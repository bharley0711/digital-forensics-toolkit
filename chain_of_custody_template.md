# Chain of Custody Form — TEMPLATE

*One form per evidence item. Complete every field at the time of collection;
add a transfer entry every time the item changes hands or location.*

## Item information

| Field | Entry |
|---|---|
| Case / matter reference | |
| Item number | |
| Item description (make, model, type) | |
| Serial number / asset tag | |
| Capacity / identifying details | |
| Condition at collection | |

## Collection

| Field | Entry |
|---|---|
| Collected by (name, organisation) | |
| Date and time collected (with timezone) | |
| Location collected from | |
| Source (device owner / custodian name) | |
| Collection method (forensic image, physical seizure, export, other) | |
| Write blocker used? (model / serial, or N/A) | |
| Acquisition tool and version | |

## Integrity verification

| Field | Entry |
|---|---|
| Hash algorithm(s) | MD5 / SHA-1 / SHA-256 |
| Acquisition hash value(s) | |
| Hash verified at acquisition? (Y/N, initials) | |
| Verification hash value(s) and date | |

## Storage

| Field | Entry |
|---|---|
| Storage location | |
| Evidence container / seal number | |
| Access restrictions | |

## Transfer log

| Date / time | Released by | Received by | Purpose | Seal intact? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## Disposition

| Field | Entry |
|---|---|
| Final disposition (returned, retained, destroyed) | |
| Date and authorisation | |

---

*Template notes: hash values are the item's integrity anchor — record them
at acquisition and re-verify at every transfer. If a hash ever fails to
match, stop, document the discrepancy in the transfer log, and notify the
case lead before proceeding.*
