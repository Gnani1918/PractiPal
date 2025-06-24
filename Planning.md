# PractiPal - Admin Flow Planning

## Overview

PractiPal is a SaaS product built with Django (backend) and PostgreSQL (database). It supports multi-role authentication with separate flows for Admin, Therapist, and Client. This document outlines the backend architecture and feature scope for the Admin login and management flow.

---

## Project Stack

- **Backend Framework:** Django (Django REST Framework)
- **Database:** PostgreSQL
- **Auth:** JWT with Role-Based Access Control
- **Frontend (Prebuilt):** To be integrated via API

---

## Roles and Responsibilities

### Admin
- Full access to manage therapists, clients, and system-wide settings.
- Can:
  - Login
  - Create & manage therapist accounts
  - Create subscription plans and assign to therapists
  - View analytics & audit logs
  - Manage global settings and promo codes
  - Create notification templates

### Therapist
- Restricted access based on subscription plan.
- Can:
  - Login **only if subscribed to a valid plan**
  - Access allowed features
  - Manage clients and sessions (depending on plan)
  - Team member count, API access, etc. depends on assigned plan

### Client (Customer)
- Can:
  - Register and login
  - View sessions, profile, therapists, etc.

---

## Admin-Specific Functional Scope

1. **Authentication**
   - Secure login with JWT
   - Role-based access (`is_admin` flag or role field)
   - Forgot password / email verification

2. **Therapist Management**
   - CRUD operations for therapists
   - Assign subscription plans
   - View subscription usage
   - **Therapist login is restricted until a valid subscription is assigned**
   - **Therapists can access features only based on their subscribed plan limits**

3. **Subscription Plans**
   - Create plans (e.g. number of clients, sessions/month, team members, features)
   - View therapist subscriptions per plan
   - Toggle premium features like API access, branding, etc.

4. **Promo Codes**
   - CRUD promo code entries
   - Control discount type, value, limit, expiry

5. **Analytics**
   - Dashboard for KPIs (Therapist signups, usage stats)

6. **Audit Logs**
   - Capture critical actions (e.g. login, plan changes)

7. **Notification Templates**
   - Create/update email/SMS templates
   - Store in DB with placeholders

8. **Settings**
   - General: Site name, maintenance mode
   - Notification: Enable Email/SMS
   - Session: Max session duration, buffer time

---

## Therapist Subscription Enforcement

- Therapist **cannot log in** unless:
  - They are assigned an **active subscription**
  - The subscription is **not expired or deactivated**

- Therapist dashboard access will be controlled:
  - Limits on number of clients, sessions, team members
  - Access to premium features (e.g., API, Branding) will be controlled at runtime

- Subscription Plan definition includes:
  - Usage limits: client/session/storage/team
  - Premium flags: API, Branding, Support, Popular tag
  - Free-form features list

---

### Shared Subscription Logic (Multi-Therapist under One Subscription)

- A **Subscription Plan** may allow **multiple therapists** under a single subscription.
- A **primary therapist** subscribes and manages the subscription.
- Additional **staff therapists** (team members) can be added under the same subscription, up to the team limit.
- Staff therapists can log in and use features as per the shared plan limits.
- Admin roles should support future expansion:
  - Super Admin (Full access)
  - Subscription Manager (Manage plans/therapists only)
