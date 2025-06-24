# PractiPal - Admin Flow Task Breakdown

> 🔗 Refer to [Planning1.md](./Planning1.md) for full architecture, scope, and enforcement rules.

## 🛠️ Phase 1: Project Setup & Auth

- [x] Initialize Django project with PostgreSQL
- [x] Create custom User model with roles: `Admin`, `Therapist`, `Client`
- [x] Implement JWT authentication (djangorestframework-simplejwt)
- [ ] Add email verification and password reset flow
- [x] Role-based permission classes (`IsAdmin`, `IsTherapist`, `IsClient`)

---

## 🔐 Phase 2: Admin Login Flow

- [ ] Create login API (Admin JWT + role check)
- [ ] Implement logout & token blacklist
- [ ] Admin dashboard basic structure (stats + endpoints)
- [ ] **Restrict Therapist login until a valid subscription is assigned**
- [ ] **Validate therapist subscription status during login**
- [ ] **Return subscription features in login response for frontend enforcement**

---

## 👥 Phase 3: Therapist Management

- [ ] Admin - Add Therapist API
- [ ] Admin - View/Edit/Delete Therapist
- [ ] Admin - Assign subscription to therapist
- [ ] **Therapist login blocked until subscription is assigned and active**
- [ ] Email notification on account creation

---

## 📦 Phase 4: Subscription Plans

- [x] Create `SubscriptionPlan` model with:
  - [x] Name, Description
  - [x] Monthly & Yearly Pricing
  - [x] Trial Days
  - [x] Usage Limits: Clients, Sessions, Storage, Team Members
  - [x] Premium Options: API Access, Branding, Support, Popular tag
  - [x] Extra feature list (JSON)
- [x] API to create, list, update plans
- [ ] Enforce usage limits at runtime for therapists
- [ ] **Validate therapist feature access based on their subscription plan**
- [ ] **Prevent login or dashboard access if subscription is expired/deactivated**

---

## 🏷️ Phase 5: Promo Code System

- [ ] Create Promo Code Model (type, value, limit, expiry, status)
- [ ] CRUD APIs for promo code
- [ ] Validation logic in subscription API

---

## 📊 Phase 6: Analytics & Audit Logs

- [ ] Track logins, subscription actions
- [ ] Daily therapist sign-up count
- [ ] Store audit logs in separate model
- [ ] Admin API to view logs (with filters)

---

## 📨 Phase 7: Notifications

- [ ] NotificationTemplate Model
- [ ] API to manage email/SMS templates
- [ ] Use templates in therapist welcome mail, etc.

---

## ⚙️ Phase 8: Settings Panel

- [ ] General Settings:
  - [ ] Site Name
  - [ ] Maintenance Mode
  - [ ] Allow new registrations
- [ ] Notification Settings:
  - [ ] Enable Email / SMS toggles
- [ ] Session Settings:
  - [ ] Max session duration
  - [ ] Session buffer time

---

## 🧪 Final Phase: Testing & Integration

- [ ] Write unit & integration tests for all admin APIs
- [ ] Document API endpoints (Swagger / ReDoc)
- [ ] Connect with frontend (Admin panel)
- [ ] Review and QA
