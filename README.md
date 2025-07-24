# Unified School Management System - Phase 1: Enrollment & Scheduling

This document outlines the project plan for Phase 1 of the Unified School Management System. The primary goal of this phase is to build a robust, flexible, and unified core system that handles the complete enrollment and scheduling process for various educational institutions in the Philippines, including those offering Basic Education, Tertiary (BS/Diploma) courses, and TESDA TVET programs.

---

## 🎯 Project Objectives

1.  **Unified Platform:** To create a single, web-based system capable of managing enrollment and scheduling for Basic Education (DepEd K-12), Tertiary Education (BS & Diploma Courses), and Technical-Vocational Education (TESDA Programs).
2.  **Flexible Scheduling Engine:** To build a powerful scheduling module that handles subject/class scheduling, faculty loading, and room assignment with conflict detection and easy modification capabilities.
3.  **Role-Centric Dashboards:** To provide clear, uncluttered dashboards tailored to the specific needs of administrators overseeing Basic Ed, College, and TVET operations.
4.  **Automated Registration Output:** To generate a comprehensive student registration form (the "White Form") that includes student data, enrolled subjects, class schedules, and a detailed breakdown of fees.
5.  **Foundation for Growth:** To build a solid technical foundation (database and architecture) that will seamlessly support future modules like Grading, Billing, and a Student Portal.

---

## 🏗️ Architecture & Technology Stack

This section outlines the recommended technology stack and deployment model chosen to meet the project's complex requirements for scalability, security, and long-term maintainability.

### Core Framework Choice: Django vs. CodeIgniter 4

Given the scope of the project, the strong recommendation is **Django**. Its "batteries-included" philosophy and structured nature are ideal for a data-intensive application like a School Management System.

| Feature | CodeIgniter 4 (PHP) | Django (Python) | Recommendation for Your SMS |
| :--- | :--- | :--- | :--- |
| **Development Speed** | Fast for simple projects. Requires adding many third-party libraries for core functions (auth, admin panels). | **Extremely fast for complex projects.** Comes with a built-in, production-ready Admin Panel, User Authentication system, and a powerful ORM. | **Django.** The built-in Admin Panel will dramatically accelerate the development of Sprint 1 (User Management, Academic Offerings, etc.). |
| **Structure & Philosophy** | "Freedom and Flexibility." Un-opinionated, giving developers more choice. | "Batteries Included & Convention over Configuration." Opinionated, providing a clear, structured way to build things. | **Django.** For a large, long-term project, Django's structure enforces clean, maintainable code, which is crucial for reducing technical debt. |
| **Security** | Provides helpers for security, but implementation is largely up to the developer. | Provides robust, built-in protection against common web vulnerabilities like CSRF, XSS, and SQL Injection by default. | **Django.** Security is non-negotiable when handling student data. Django's "secure-by-default" approach is a major advantage. |
| **Talent Pool (Philippines)** | **Excellent.** PHP is the most common web development language in the Philippines, making it easy to find CI4 developers. | **Very Good & Growing.** The Python community is expanding rapidly. The long-term benefits of Django outweigh the slightly larger PHP talent pool. | While the PHP talent pool is vast, the productivity gains from Django's features make it the superior choice for this specific application. |

### Recommended Full Tech Stack

This stack is modern, highly productive, and designed for building robust, enterprise-grade web applications.

#### Backend
* **Framework:** **Django 5.x**
    * **Why:** Its "batteries-included" approach provides the Admin Panel, ORM, and security features that are perfect for an SMS.
* **API Layer:** **Django REST Framework (DRF)**
    * **Why:** The industry standard for building powerful and flexible APIs with Django. It will be the communication layer between the backend and frontend.
* **Background Tasks:** **Celery with Redis**
    * **Why:** For time-consuming tasks like generating large reports. This ensures the application remains fast and responsive for the user.
* **Application Server:** **Gunicorn**
    * **Why:** A mature and reliable WSGI HTTP Server that will run the Django application on the server.

#### Frontend
* **Framework:** **Vue.js 3**
    * **Why:** It offers a gentler learning curve than React, has outstanding documentation, and is incredibly performant. Its component-based architecture is perfect for building a complex UI.
* **Build Tool:** **Vite**
    * **Why:** The modern standard for frontend tooling, providing a lightning-fast development server and optimized production builds.
* **UI Component Library:** **Vuetify 3** or **Quasar Framework**
    * **Why:** A massive time-saver. These libraries provide a complete set of pre-built, professional, and responsive UI components (data tables, forms, modals, etc.).
* **State Management:** **Pinia**
    * **Why:** The official, intuitive state management library for Vue.js, perfect for managing application-wide data.

#### Database
* **Database:** **PostgreSQL 16**
    * **Why:** The preferred database for Django. It's a powerful, open-source database known for its reliability and performance with complex queries.

#### Development & Deployment Environment
* **Containerization:** **Docker & Docker Compose**
    * **Why:** This is a modern best practice. It guarantees that the development environment is **identical** to the production environment on the school's LAN server, eliminating "it works on my machine" problems and simplifying deployment.

### Deployment Model & On-Premise Server Setup

This system will be deployed using an **on-premise (LAN-based) model**. The application will be installed on a dedicated server located at the client's school.

* **Hardware Requirements (Client-Provided Server):**
    * **Server Type:** A reliable tower server or rack-mount server (e.g., Dell PowerEdge T-series, HPE ProLiant ML-series).
    * **Processor (CPU):** A modern multi-core server processor (e.g., Intel® Xeon® E-2300 series or equivalent).
    * **Memory (RAM):** 16 GB minimum. **32 GB is highly recommended**.
    * **Storage (Drives):** **SSDs are essential.** Recommended setup: **2 x 1TB SSDs in a RAID 1 configuration** for data redundancy.
    * **Network:** Standard 1 Gigabit Ethernet port.
    * **Backup Solution:**
        > **CRITICAL:** The client is responsible for maintaining a separate, independent backup solution (e.g., external HDD or NAS).

* **Software Stack (To be installed via Docker):**
    * **Operating System:** Ubuntu Server 24.04 LTS (Linux) is recommended as the host OS for Docker.
    * **Web Server / Reverse Proxy:** Nginx.
    * **Database:** PostgreSQL.
    * **Application:** Django + Gunicorn.
    * **Caching/Broker:** Redis.

---

## 🚀 Project Sprints

The project is broken down into four distinct sprints, each building upon the last.

### Sprint 1: 🏗️ The Foundation & Core Configuration
> **Sprint Goal:** To establish the basic data structures, user roles, and configuration panels that will underpin the entire system using Django's built-in capabilities.
>
> **Estimated Duration:** 15-20 Developer-Days

| Feature / Task | Est. Time | User Stories |
| :--- | :--- | :--- |
| **User & Role Management** | 3 days | **As an Administrator,** I want to create user accounts and assign roles (Admin, Registrar, Academic Head, Scheduler) so that I can control access to different parts of the system. |
| **Academic Year & Period Setup** | 2 days | **As an Admin,** I want to define Academic Years (e.g., SY 2025-2026) and periods (Semesters for College, Trimesters for Diploma, Full Year for Basic Ed) so that all data is correctly compartmentalized. |
| **Student Profile Management (SIS Core)** | 4 days | **As a Registrar,** I want to create, search, and update a comprehensive student profile (including personal info, contact details, and photo) to maintain a single source of truth for every student. |
| **Faculty Profile Management** | 2 days | **As an Academic Head,** I want to manage a database of faculty members/trainers, including their contact details and qualifications, so I can assign them to subjects later. |
| **Unified Academic Offerings** | 4 days | **As an Academic Head,** I want to define all available academic offerings (e.g., "Grade 11 - ABM", "BS in IT", "Cookery NC II", "3-Yr Diploma in Hospitality") so that they are ready for enrollment. |

### Sprint 2: ⚙️ The Unified Enrollment Engine
> **Sprint Goal:** To build the core enrollment workflow, allowing a registrar to enroll any type of student into any academic offering.
>
> **Estimated Duration:** 20-25 Developer-Days

| Feature / Task | Est. Time | User Stories |
| :--- | :--- | :--- |
| **Main Enrollment Interface** | 6 days | **As a Registrar,** I want a single interface to search for a student and enroll them into a specific Academic Offering and Academic Year so that the process is efficient and standardized. |
| **Document & Requirements Tracking**| 3 days | **As a Registrar,** I want a checklist of required documents (Form 137, PSA Cert) for each enrollment and mark them as submitted, so we can track compliance. |
| **Initial Fee Assessment** | 4 days | **As an Admin,** I want to pre-define tuition and miscellaneous fees for each Academic Offering. **As a Registrar,** I want the system to automatically calculate the initial fees upon enrollment so that the student knows their financial obligation. |
| **Enrollment Status Management** | 2 days | **As a Registrar,** I want to manage a student's enrollment status (e.g., Pending, Enrolled, Reserved, Cancelled) to maintain accurate enrollment counts. |
| **Subject/Course Loading for Enrollment** | 5 days | **As an Academic Head,** I want to pre-load a set of subjects/courses for each offering (e.g., all Grade 7 subjects, all 1st-Year IT subjects). **As a Registrar,** I want these subjects to be automatically attached to a student upon enrollment. |

### Sprint 3: ⚡ The Scheduling Powerhouse
> **Sprint Goal:** To develop the visual and logical tools for creating class schedules, assigning faculty, and managing resources without conflicts.
>
> **Estimated Duration:** 25-30 Developer-Days

| Feature / Task | Est. Time | User Stories |
| :--- | :--- | :--- |
| **Room & Facility Management** | 2 days | **As an Admin,** I want to create a database of all available rooms and facilities (e.g., Room 101, Computer Lab 1, Kitchen Lab) so they can be assigned to classes. |
| **Faculty Loading** | 5 days | **As an Academic Head,** I want to assign specific subjects to qualified faculty members for a given academic period so that teaching loads are clear. |
| **Visual Class Schedule Creator** | 10 days | **As a Scheduler,** I want a visual, grid-based interface to create class schedules by selecting a subject, assigning a faculty member and room, and placing it into a time slot. |
| **Conflict Detection Engine** | 5 days | **As a Scheduler,** I want the system to automatically prevent me from scheduling the same teacher, same section, or same room in two different classes at the same time. |
| **Dynamic Schedule Adjustment** | 3 days | **As an Administrator,** I want to easily edit a created schedule (change the teacher, move the time/day, or change the room) to accommodate unforeseen changes. |

### Sprint 4: 📊 Dashboards, Reporting & TVET Specialization
> **Sprint Goal:** To provide administrators with actionable data through dashboards, produce the final enrollment form, and build the specialized TVET assessment scheduling workflow.
>
> **Estimated Duration:** 20-25 Developer-Days

| Feature / Task | Est. Time | User Stories |
| :--- | :--- | :--- |
| **Role-Based Dashboards** | 6 days | **As a School Director,** I want separate dashboards for Basic Ed, College, and TVET, each showing key metrics like total enrollees, enrollment trends, and fee collection summaries. |
| **Registration Form ("White Form") Generation** | 5 days | **As a Registrar,** I want to print a comprehensive "White Form" for any enrolled student that contains their photo, personal info, a list of their subjects with the final schedule (day, time, room, faculty), and a detailed breakdown of fees. |
| **TESDA Training Scheduling** | 4 days | **As a TVET Coordinator,** I want to define the specific training duration (in hours/days/weeks) and pre-assign a trainer for each TESDA qualification, separate from the main scheduling module. |
| **TESDA Assessment Scheduling**| 5 days | **As a TVET Assessment Coordinator,** I want a dedicated interface to schedule assessment dates for a qualification and book individuals or a full batch (10 pax) into that assessment schedule. |

---

## ⚠️ Disclaimer

The estimated developer-days are for planning purposes and assume a focused development effort. Actual timelines can vary based on team size, complexity discovered during development, and client feedback cycles.
