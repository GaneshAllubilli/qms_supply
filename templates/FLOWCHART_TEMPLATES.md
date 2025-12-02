# QMS Flowchart Template

## Instructions for Creating Flowcharts

You can create flowcharts using:
1. **Hand-drawn** (recommended for authenticity): Draw on paper and scan/photograph
2. **Digital tools**: Draw.io, Lucidchart, Microsoft Visio, PowerPoint
3. **Text-based** (for quick drafts): Using ASCII or Markdown

---

## Flowchart Symbols Guide

```
┌─────────┐
│ Process │  = Rectangular box for actions/processes
└─────────┘

    ◇       = Diamond for decisions (Yes/No questions)
   / \
  /   \

   ___
  (   )     = Oval/Circle for Start/End points
   ‾‾‾

   ───►     = Arrow showing flow direction

┌─────────┐
│Document │  = Document symbol (wavy bottom)
└─────────┘
```

---

## Template 1: Basic Module Workflow

```
    START
      │
      ▼
┌──────────────┐
│ Create New   │
│ Record       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Fill Form    │
│ Fields       │
└──────┬───────┘
       │
       ▼
     ◇ Valid?
    / \
   /   \
  Yes   No
   │     │
   │     └──► [Return to Form]
   │
   ▼
┌──────────────┐
│ Submit for   │
│ Review       │
└──────┬───────┘
       │
       ▼
     ◇ Approved?
    / \
   /   \
  Yes   No
   │     │
   │     └──► [Request Changes]
   │
   ▼
┌──────────────┐
│ Close/       │
│ Complete     │
└──────┬───────┘
       │
       ▼
     END
```

---

## Template 2: Deviation Management Flow

```
START: Deviation Detected
         │
         ▼
┌────────────────────┐
│ Report Deviation   │
│ (Production Mgr)   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Assign to QA       │
│ Officer            │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Investigate        │
│ Root Cause         │
└─────────┬──────────┘
          │
          ▼
       ◇ Severity?
      / │ \
     /  │  \
Critical│Minor
    │   │   │
    │   │   └──► [Document & Close]
    │   │
    │   └──► [Implement Quick Fix]
    │
    ▼
┌────────────────────┐
│ Initiate CAPA      │
└─────────┬──────────┘
          │
          ▼
        END
```

---

## Template 3: CAPA Workflow

```
START: CAPA Initiated
         │
         ▼
┌────────────────────┐
│ Define Problem     │
│ Statement          │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Root Cause         │
│ Analysis (5 Why's) │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Develop Action     │
│ Plan               │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Assign             │
│ Responsibilities   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Implement          │
│ Actions            │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Verify             │
│ Effectiveness      │
└─────────┬──────────┘
          │
          ▼
       ◇ Effective?
      / \
     /   \
   Yes    No
    │      │
    │      └──► [Revise Action Plan]
    │
    ▼
┌────────────────────┐
│ Close CAPA         │
└─────────┬──────────┘
          │
          ▼
        END
```

---

## Template 4: Product Complaint Flow

```
START: Complaint Received
         │
         ▼
┌────────────────────┐
│ Log Complaint      │
│ Details            │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Acknowledge to     │
│ Customer           │
└─────────┬──────────┘
          │
          ▼
       ◇ Severity?
      / │ \
     /  │  \
  High Med Low
    │   │   │
    │   │   └──► [Standard Investigation]
    │   │
    │   └──► [Priority Investigation]
    │
    ▼
┌────────────────────┐
│ Urgent             │
│ Investigation      │
└─────────┬──────────┘
          │
          ▼
       ◇ Recall Needed?
      / \
     /   \
   Yes    No
    │      │
    │      └──► [Continue Investigation]
    │
    ▼
┌────────────────────┐
│ Initiate Recall    │
│ Process            │
└─────────┬──────────┘
          │
          ▼
        END
```

---

## Template 5: Recall Management Flow

```
START: Recall Decision
         │
         ▼
┌────────────────────┐
│ Classify Recall    │
│ Type & Scope       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Identify Affected  │
│ Batches            │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Notify Regulatory  │
│ Authorities        │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Notify Customers/  │
│ Distributors       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Track Product      │
│ Returns            │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Verify Recall      │
│ Effectiveness      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Submit Final       │
│ Report             │
└─────────┬──────────┘
          │
          ▼
        END
```

---

## Template 6: Supplier Management Flow

```
START: New Supplier
         │
         ▼
┌────────────────────┐
│ Initial            │
│ Assessment         │
└─────────┬──────────┘
          │
          ▼
       ◇ Meets Criteria?
      / \
     /   \
   Yes    No
    │      │
    │      └──► [Reject Supplier]
    │
    ▼
┌────────────────────┐
│ Conduct Audit      │
└─────────┬──────────┘
          │
          ▼
       ◇ Audit Pass?
      / \
     /   \
   Yes    No
    │      │
    │      └──► [Request Improvements]
    │
    ▼
┌────────────────────┐
│ Approve Supplier   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Ongoing            │
│ Monitoring         │
└─────────┬──────────┘
          │
          ▼
       ◇ Performance OK?
      / \
     /   \
   Yes    No
    │      │
    │      └──► [Initiate CAPA]
    │
    ▼
   [Continue Monitoring]
```

---

## Template 7: Role-Based Workflow

### QA Officer Daily Workflow

```
START: Daily Tasks
         │
         ├──► Review New Deviations
         │
         ├──► Investigate Complaints
         │
         ├──► Monitor CAPA Progress
         │
         ├──► Approve Documents
         │
         ├──► Conduct Audits
         │
         └──► Generate Reports
              │
              ▼
            END
```

### Production Manager Daily Workflow

```
START: Daily Tasks
         │
         ├──► Report Deviations
         │
         ├──► Implement CAPAs
         │
         ├──► Review Batch Records
         │
         ├──► Coordinate with QA
         │
         └──► Monitor Production Quality
              │
              ▼
            END
```

---

## Template 8: Integration Flow

```
┌─────────────┐
│ Deviation   │
│ Management  │
└──────┬──────┘
       │
       ▼
    ◇ Critical?
   / \
  /   \
Yes    No
 │      │
 │      └──► [Document Only]
 │
 ▼
┌─────────────┐
│    CAPA     │
└──────┬──────┘
       │
       ▼
    ◇ Customer Impact?
   / \
  /   \
Yes    No
 │      │
 │      └──► [Internal Only]
 │
 ▼
┌─────────────┐
│  Product    │
│ Complaints  │
└──────┬──────┘
       │
       ▼
    ◇ Widespread?
   / \
  /   \
Yes    No
 │      │
 │      └──► [Individual Response]
 │
 ▼
┌─────────────┐
│   Recall    │
│ Management  │
└─────────────┘
```

---

## Tips for Creating Effective Flowcharts

1. **Keep it Simple**: Don't overcomplicate
2. **Use Consistent Symbols**: Stick to standard flowchart symbols
3. **Label Clearly**: Make sure each step is clearly labeled
4. **Show Decision Points**: Use diamonds for yes/no decisions
5. **Indicate Roles**: Show who is responsible for each step
6. **Add Notes**: Include important details or exceptions
7. **Test the Flow**: Walk through the flowchart to ensure it makes sense

---

## Recommended Tools

### Free Tools:
- **Draw.io** (diagrams.net) - Web-based, free
- **Google Drawings** - Simple and collaborative
- **Microsoft PowerPoint** - Using shapes and connectors
- **Pen and Paper** - Most authentic for this assignment!

### Paid Tools:
- **Lucidchart** - Professional flowcharting
- **Microsoft Visio** - Industry standard
- **Miro** - Collaborative whiteboard

---

## Submission Format

When creating your flowcharts:
1. Create one flowchart per module (6 total)
2. Include role-based perspectives
3. Show integration points between modules
4. Add legends explaining symbols used
5. Include API and Raw Material example flows

Save as:
- `flowchart_deviation_management.png/pdf`
- `flowchart_capa.png/pdf`
- `flowchart_product_complaints.png/pdf`
- `flowchart_recall_management.png/pdf`
- `flowchart_adverse_events.png/pdf`
- `flowchart_supplier_management.png/pdf`
