# Amazon SP-API (Seller Central & Vendor Central)

This repository contains reference assets and integration examples for working with **Amazon Selling Partner API (SP-API)** for:

- **Amazon Seller Central**
- **Amazon Vendor Central**

The goal is to extract Amazon operational data and prepare it for downstream analytics tools such as **Power BI**, following the same philosophy used in the Shopify REST API repository.

---

## Overview

Amazon SP-API is Amazon’s unified REST API that replaces legacy MWS and Vendor APIs.  
It supports both **Seller Central** and **Vendor Central** data access through different API groups.

This repository focuses on:
- Understanding available endpoints
- Authentication requirements
- Common datasets used for ecommerce analytics
- Power BI–friendly data extraction patterns

---

## Supported Amazon Accounts

### Seller Central (SP-API Seller)
Typical use cases:
- Orders & order items
- FBA inventory summaries
- Listings & catalog data
- Financial events / settlements
- Returns (availability varies)

### Vendor Central (SP-API Vendor)
Availability depends on vendor enrollment:
- Retail Procurement (POs, shipments, invoices)
- Direct Fulfillment (dropship orders, acknowledgements, shipments)

---

## Authentication (High Level)

Amazon SP-API requires **multiple layers of authentication**:

1. **Login with Amazon (LWA)**  
   - Client ID  
   - Client Secret  

2. **AWS IAM**
   - IAM User or Role
   - SP-API–specific IAM policy

3. **SP-API Application Registration**
   - Application ID
   - Authorization scopes
   - Refresh token (depending on authorization model)

All API calls must be **signed with AWS SigV4**.

> Do not store credentials in source control.

---

## API Endpoint Categories

### Seller Central APIs
- Orders API
- Catalog Items API
- Listings Items API
- FBA Inventory API
- Reports API
- Finances API

### Vendor Central APIs
- Vendor Orders API
- Vendor Shipments API
- Vendor Invoices API
- Vendor Direct Fulfillment APIs

Not all endpoints are available to every account.

---

## Rate Limits

Amazon enforces **strict rate limits** per operation.

Best practices:
- Implement retry with exponential backoff
- Batch requests where supported
- Cache reference data (SKUs, ASINs)

Failure to respect rate limits may result in temporary throttling.

---

## Power BI Integration Pattern

Direct SP-API connections from Power BI are **not recommended** due to:
- OAuth + AWS SigV4 complexity
- Refresh instability
- Credential rotation requirements

### Recommended Flow

SP-API  
→ Scheduled extractor (Python / Azure Function / Lambda)  
→ SharePoint / OneDrive (CSV or Parquet)  
→ Power BI (SharePoint Folder connector)

Use a `latest/` folder pattern so Power BI refreshes do not break.

---

## Common Datasets for BI

Seller Central:
- Orders
- Order Items
- Inventory Snapshots
- Fees & settlements

Vendor Central:
- Purchase Orders
- Shipments
- Invoices
- Fill rate & lead time metrics

These datasets typically map well to a **star schema**:
- `dim_date`
- `dim_sku`
- Fact tables per dataset

---

## Notes

- SP-API access must be approved by Amazon
- Vendor APIs require explicit vendor authorization
- API availability and data depth vary by account
- Always validate data against Seller/Vendor Central UI reports

---

## Reference

- Amazon Selling Partner API Overview  
  https://developer.amazonservices.com/start

- Vendor API Overview  
  https://developer.amazonservices.com/vendor-api

---

## License

Internal use only.  
Structure and intent mirror the Shopify REST API reference repository.

