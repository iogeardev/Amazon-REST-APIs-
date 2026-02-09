"""Vendor Direct Fulfillment extractor (skeleton).

Writes:
- Raw CSV into exports/raw/vendor/
- Modeled CSV into exports/modeled/vendor/

Replace stubs with real SP-API client calls.
"""

import csv
from pathlib import Path
from datetime import date

from Amazon.scripts.utils.logging import get_logger

logger = get_logger()

def main():
    today = date.today().isoformat()

    raw_dir = Path("Amazon/exports/raw/vendor")
    modeled_dir = Path("Amazon/exports/modeled/vendor")
    raw_dir.mkdir(parents=True, exist_ok=True)
    modeled_dir.mkdir(parents=True, exist_ok=True)

    # TODO: call SP-API and collect rows
    rows = [
        "purchaseOrderNumber":"DFPO123","orderDate":"2026-02-01","shipmentDate":"2026-02-02","trackingNumber":"1Z999"
    ]

    raw_path = raw_dir / "direct_fulfillment_" + today + ".csv"
    modeled_path = modeled_dir / "fact_direct_fulfillment.csv"

    # raw
    with open(raw_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    # modeled (placeholder: same as raw)
    with open(modeled_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    logger.info("Wrote %s and %s", raw_path, modeled_path)

if __name__ == "__main__":
    main()
