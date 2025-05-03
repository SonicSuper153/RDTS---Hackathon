# RDTS---Hackathon

Agentic AI for Cloud Operations
1. Domain / Themes
Generative AI & Natural‑Language Interfaces
Cloud Infrastructure Automation (OpenStack)
2. Background / Context
Cloud operators routinely perform tasks such as creating, resizing, or deleting VMs, volumes, and networks. Today this requires translating intent into a series of CLI commands or API calls. AceCloud challenges participants to build an agentic AI that accepts natural‑language instructions, plans the required OpenStack API calls, and executes them after a confirmation step—returning results conversationally.

3. Objectives
The solution must:

Parse natural‑language requests (questions or instructions) using an LLM or intent–entity model.
Map each intent to the corresponding CRUD actions across OpenStack Compute (Nova), Network (Neutron), and Block‑Storage (Cinder) APIs.
Ask for explicit confirmation (Yes/No) before executing any create, resize, or delete action, then report the outcome.
Provide informational answers such as project usage or quota status on demand.
The solution should be secure through TLS encryption over APIs.
A Database must be maintained of user requests
4. Functional Requirements
#

Scenario

Expected Behaviour

FR‑1

VM Provisioning

“Create an S.4 VM named dev‑box.” → Model confirms, launches the instance, then returns its ID and IP.

FR‑2

VM Resizing

“Resize dev‑box to flavor M.8.” → Model confirms, performs the resize, and reports success.

FR‑3

VM Deletion

“Delete the VM dev‑box.” → Model confirms destruction and removes the server.

FR‑4

Network Creation

“Create a private network called blue‑net.” → Model confirms, creates network + subnet, returns details.

FR‑5

Volume Operations

“Create a 100 GB volume named data‑disk.” / “Delete volume data‑disk.” → Model confirms and executes.

FR‑6

Usage Query

“What’s my project usage?” → Returns aggregate vCPU, RAM, GPU, and volume consumption.

5. Technical Requirements & Constraints
Open Technology Choice: Any modern web, backend, and ML stack may be used. Containerised deployment is recommended.
Performance: End‑to‑end conversational latency ≤ 2 seconds for basic intents.
Testing: Provide automated tests covering at least two happy‑path and two negative dialog flows.
Confirmation: Every resource‑modifying operation (create, resize, delete) must be preceded by a confirmation prompt.
6. Deliverables
Working Demo: Hosted instance or recorded video demonstrating all functional scenarios.
Source Repository: Public Git repository with build instructions and deployment artefacts (Docker/Helm/etc.).
Documentation:
Architecture overview
Dialog‑flow diagrams
Test‑case matrix
Optional: Slide deck (≤ 10 slides) summarizing design and learnings.
7. Evaluation Criteria
Weight

Criterion

Details

40 %

Functional Correctness

CRUD operations executed accurately via OpenStack APIs with confirmations

25 %

Agent Intelligence

Intent detection, slot filling, and robust disambiguation

15 %

Code Quality & DevOps Readiness

Clean architecture, tests, reproducible deployment

10 %

User Experience

Clarity and usefulness of conversational interaction

10 %

Innovation

Extensions beyond required scenarios

8. Resources Provided
AceCloud OpenStack sandbox credentials
API reference documentation

S.no

Service

Service Endpoint

1

Cloudformation

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8000/v1

2

Clustering

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8778

3

Compute

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1

4

Compute_Legacy

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2/a02b14bcfca64e44bd68f2d00d8555b5

5

Identity

https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000

6

Image

https://api-ap-south-mum-1.openstack.acecloudhosting.com:9292

7

Key Manager

https://api-ap-south-mum-1.openstack.acecloudhosting.com:9311

8

Load Balancer

https://api-ap-south-mum-1.openstack.acecloudhosting.com:9876

9

Metric

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8041

10

Network

https://api-ap-south-mum-1.openstack.acecloudhosting.com:9696

11

Orchestration

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8004/v1/a02b14bcfca64e44bd68f2d00d8555b5

12

Placement

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8780

13

Volumev3

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3/a02b14bcfca64e44bd68f2d00d8555b5

14

Workflowv2

https://api-ap-south-mum-1.openstack.acecloudhosting.com:8989/v2

 

 

 

 

 

 

 

USER

Hackathon_AIML_1

 

PASSWORD

Hackathon_AIML_1@567
