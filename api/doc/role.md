# Role module

## Bug: argument order mismatch in `find_one` / `find_by_id`

`RoleRepository.find_one` is defined as `find_one(self, id, session)`, matching
the convention used across the rest of the codebase (see
`UserRepocitory.find_one`, `UserServices.update/delete`, `UserController`):
the resource identifier always comes before `session`.

`RoleServices.find_one`, however, was defined as `find_one(self, session, id)`
— the two parameters swapped relative to every other service method — and it
forwarded them in that same swapped order to the repository:

```python
# before
def find_one(self, session, id):
    return role_repository.find_one(session, id)
```

`RoleController.find_by_id` calls `role_services.find_one(id, session)`
positionally, following the codebase-wide `(id, session)` convention. Because
`RoleServices.find_one`'s parameters were named in the opposite order, the
`id` value was bound to the local variable `session` and the actual session
object was bound to the local variable `id`. It then forwarded those two
(mismatched-name-but-still-positionally-`id`-then-`session`) values on to
`role_repository.find_one(session, id)`, which by coincidence landed back in
the correct `(id, session)` slots on the repository.

In other words, the current behavior was correct only by accident — two
swaps cancelling out — not because the code was correct. That makes it a real
bug: any change to either call site (making it consistent with the
`find_one(id, session)` naming actually declared in the service) would silently
break lookups by passing the `Session` object where an integer `id` is
expected, e.g. `Role.id == <Session object>`.

### Fix

`RoleServices.find_one` now uses the same `(id, session)` order and names as
`RoleRepository.find_one` and every other service in the project:

```python
# after
def find_one(self, id, session):
    return role_repository.find_one(id, session)
```

No changes were needed in `RoleController.find_by_id` — it already called
`role_services.find_one(id, session)` in the project's standard order; it
just needed the service underneath to actually mean what its call site
assumed.

### Other cleanup in `role_repository.py`

- Removed the unused `Session` import (`from sqlmodel import select, Session`)
  — it was never referenced.
- Fixed the over-indented body of `find_one` (12 spaces instead of 8) to
  match `find_all` and the rest of the codebase's style.

## `RoleController` inconsistencies

Separately from the argument-order bug above, `RoleController.find_by_id` did
not match the conventions used by its sibling method `list_roles` (and by
`UserController` elsewhere in the project):

- `id` had no type hint, while every other controller method that takes an
  `id` (`UserController.update_user`, `delete_user`) declares it as `id: int`.
- It had no return type annotation, while `list_roles -> RoleData` does.
- It returned the raw `Role` SQLModel instance straight from the database
  instead of going through the `RoleResponse` DTO the way `list_roles` builds
  `RoleData` from `RoleResponse`. Returning the ORM model directly bypasses
  the DTO layer's validation (`ValidRoleName`) and couples the API response
  shape to the database model, so any future column added to `Role` (e.g. an
  internal flag) would leak into the JSON response unless the controller is
  updated.

### Fix

```python
def find_by_id(self, id: int, session) -> RoleResponse:
    role = self.role_services.find_one(id, session)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return RoleResponse(**role.model_dump())
```

`find_by_id` now type-hints `id: int`, declares `-> RoleResponse`, and maps
the `Role` model through `RoleResponse` before returning it, keeping the
response shape explicit and consistent with `list_roles`.

## Reference

| Layer | Method | Signature |
|---|---|---|
| `RoleRepository` | `find_one` | `(self, id, session)` |
| `RoleServices` | `find_one` | `(self, id, session)` |
| `RoleController` | `find_by_id` | `(self, id, session)` — raises `HTTPException(404)` when the role does not exist |

All three layers now agree on argument order: `id` first, `session` second.
