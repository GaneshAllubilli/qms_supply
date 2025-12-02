# Manual QMS Exploration Guide

## Step-by-Step Instructions

Since the automated navigation needs refinement, follow these manual steps to explore each QMS module:

### Prerequisites
1. Open Microsoft Edge browser
2. Navigate to: http://216.48.184.249:5274/quality
3. Login with:
   - Email: testing@aivoa.net
   - Password: password123

### Exploration Checklist

For each module below, please:
1. Navigate to the module
2. Take a screenshot (save as `[module_name].png`)
3. Document the following:
   - **Form Fields**: List all input fields and their types
   - **Workflow Steps**: Identify the process flow (Draft → Submit → Review → Approve, etc.)
   - **Key Features**: Note any special functionality
   - **Role Actions**: What can a QA Officer vs Production Manager do?

---

## Module 1: Deviation Management (In-Process Quality)

### What to Look For:
- **Deviation ID**: Auto-generated or manual?
- **Deviation Type**: Dropdown options
- **Severity Level**: Critical, Major, Minor
- **Product/Material Affected**: API or Raw Material
- **Root Cause Analysis**: Text field
- **Corrective Actions**: What actions can be taken?
- **Approval Workflow**: Who approves?
- **Status Tracking**: Open, Under Investigation, Closed

### Example Scenarios to Document:
1. **API Example**: Deviation in API synthesis temperature
2. **Raw Material Example**: Deviation in raw material purity

### Role Perspectives:
- **QA Officer**: Can create, investigate, and close deviations
- **Production Manager**: Can report deviations, view status

---

## Module 2: CAPA (Corrective and Preventive Actions)

### What to Look For:
- **CAPA ID**: Tracking number
- **Type**: Corrective vs Preventive
- **Source**: Deviation, Audit, Complaint, etc.
- **Problem Statement**: Description field
- **Root Cause**: Analysis section
- **Action Plan**: Steps to resolve
- **Effectiveness Check**: How is effectiveness verified?
- **Due Dates**: Timeline tracking

### Example Scenarios:
1. **API Example**: CAPA for recurring API batch failures
2. **Raw Material Example**: CAPA for supplier quality issues

### Role Perspectives:
- **QA Officer**: Initiates CAPA, tracks effectiveness
- **Production Manager**: Implements corrective actions

---

## Module 3: Product Complaints (In-Product Quality)

### What to Look For:
- **Complaint ID**: Tracking number
- **Customer Information**: Name, contact
- **Product Details**: Batch number, product name
- **Complaint Type**: Quality, packaging, efficacy
- **Severity**: Impact assessment
- **Investigation**: Root cause analysis
- **Response**: Customer communication
- **CAPA Link**: Connection to CAPA module

### Example Scenarios:
1. **API Example**: Complaint about API impurity
2. **Raw Material Example**: Complaint about contamination

### Role Perspectives:
- **QA Officer**: Investigates complaints, determines root cause
- **Production Manager**: Provides production data for investigation

---

## Module 4: Recall Management (In-Product Quality)

### What to Look For:
- **Recall ID**: Tracking number
- **Recall Type**: Voluntary vs Mandatory
- **Scope**: Batch-specific or product-wide
- **Reason**: Quality defect, contamination, etc.
- **Affected Batches**: List of batch numbers
- **Distribution**: Where products were shipped
- **Notification**: Customer/regulatory communication
- **Effectiveness**: Recall completion tracking

### Example Scenarios:
1. **API Example**: Recall due to API stability failure
2. **Raw Material Example**: Recall due to raw material contamination

### Role Perspectives:
- **QA Officer**: Initiates recall, coordinates with regulatory
- **Production Manager**: Identifies affected batches, stops production

---

## Module 5: Adverse Event Reporting (In-Product Quality)

### What to Look For:
- **Event ID**: Tracking number
- **Event Type**: Serious vs Non-serious
- **Product Information**: Batch, dosage
- **Patient Information**: Demographics (anonymized)
- **Event Description**: What happened?
- **Causality Assessment**: Related to product?
- **Regulatory Reporting**: FDA, EMA requirements
- **Follow-up**: Additional information needed?

### Example Scenarios:
1. **API Example**: Adverse reaction to API-based drug
2. **Raw Material Example**: Adverse event linked to excipient

### Role Perspectives:
- **QA Officer**: Evaluates causality, submits regulatory reports
- **Production Manager**: Provides manufacturing records

---

## Module 6: Supplier Management (QMS Management)

### What to Look For:
- **Supplier ID**: Unique identifier
- **Supplier Name**: Company name
- **Material Type**: API, Raw Material, Packaging
- **Qualification Status**: Approved, Under Review, Rejected
- **Audit Schedule**: When was last audit?
- **Quality Metrics**: Defect rates, on-time delivery
- **Certificates**: COA, GMP certificates
- **CAPA Tracking**: Supplier-related CAPAs

### Example Scenarios:
1. **API Supplier**: Qualification of new API manufacturer
2. **Raw Material Supplier**: Audit of excipient supplier

### Role Perspectives:
- **QA Officer**: Qualifies suppliers, conducts audits
- **Production Manager**: Evaluates supplier performance

---

## Data Collection Template

For each module, fill out:

```
Module Name: _______________
Date Explored: _______________

1. Primary Purpose:
   [Brief description]

2. Key Form Fields:
   - Field 1: [Name] - [Type] - [Purpose]
   - Field 2: [Name] - [Type] - [Purpose]
   ...

3. Workflow Steps:
   Step 1: [Action] → Step 2: [Action] → Step 3: [Action]

4. API Example:
   [Detailed scenario]

5. Raw Material Example:
   [Detailed scenario]

6. QA Officer Perspective:
   [What they can do, their responsibilities]

7. Production Manager Perspective:
   [What they can do, their responsibilities]

8. Integration Points:
   [How this module connects to others]
```

---

## Next Steps After Manual Exploration

1. Compile all screenshots into a folder
2. Fill out the data collection template for each module
3. Create flowcharts showing:
   - End-to-end process for each module
   - Role-based workflows
   - Integration between modules
4. Prepare presentation/document with:
   - Module overviews
   - Workflow diagrams
   - Real-world examples
   - Role perspectives

---

## Tips for Effective Exploration

1. **Take Detailed Notes**: Document everything you see
2. **Try Creating Records**: If possible, create test entries
3. **Check Permissions**: Note what different roles can access
4. **Look for Integrations**: How do modules connect?
5. **Identify Pain Points**: What could be improved?
6. **Think Real-World**: How would this work in an actual pharma company?

---

## Questions to Answer

1. How does a deviation lead to a CAPA?
2. How does a complaint trigger a recall?
3. How are adverse events linked to product complaints?
4. How does supplier management impact deviation tracking?
5. What reports can be generated from each module?
6. How is regulatory compliance ensured?
