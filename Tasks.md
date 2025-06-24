# PractiPal - Admin Flow Tasks

This document outlines development tasks based on the planning for the PractiPal Admin module. Each task should be completed with test coverage, security checks, OpenAPI documentation, and frontend integration using the `practipal-frontend` structure.

---

## ✅ General Guidelines for All Tasks

- Read the corresponding frontend structure and API usage before implementing
- Write secure, optimized, production-grade Django code
- Use JWT authentication with role-based permissions
- Follow drf-spectacular (OpenAPI 3.0) for documentation
- Enforce subscription-based access control
- Cache-read-heavy endpoints with `django-redis` and `cacheops`
- Test every API independently and after frontend integration
- After completing each task:
  - ✅ Mark it completed in this file
  - 🔁 Move to the next task

---

## 📌 Phase 1: Authentication & Role Access

- [ ] Implement Admin login using JWT
- [ ] Add role field (`Admin`, `Therapist`, `Client`) and enforce access
- [ ] Add password reset, email verification flows
- [ ] Create Super Admin and Subscription Manager roles
- [ ] Add middleware for enforcing authenticated access

---

## 📌 Phase 2: Therapist Management

- [ ] Create Therapist model (extend User)
- [ ] Admin: CRUD operations for therapists
- [ ] Assign subscription to therapist during onboarding
- [ ] Restrict therapist login unless they are subscribed
- [ ] Support shared subscriptions (team therapists)
- [ ] View usage metrics (sessions, clients) per therapist

---

## 📌 Phase 3: Subscription Plans

- [ ] Create SubscriptionPlan model
- [ ] Add fields: name, price, client/session limits, team member count
- [ ] Support premium flags: API Access, Branding, Support, Popular
- [ ] Allow custom features (free text)
- [ ] Assign plans to therapists during onboarding
- [ ] View therapists under each plan

---

## 📌 Phase 4: Promo Code Management

- [ ] Model: PromoCode (type, value, usage limit, status, expiry)
- [ ] Admin: Create/update/delete promo codes
- [ ] Validate promo codes during therapist subscription

---

## 📌 Phase 5: Analytics Dashboard

- [ ] KPIs: New signups, active therapists, plan usage
- [ ] Time series graphs: weekly/monthly metrics
- [ ] Expose analytics APIs with role-based access

---

## 📌 Phase 6: Audit Logs

- [ ] Model: AuditLog (user, action, timestamp, details)
- [ ] Log critical actions: login, plan change, promo use, settings update
- [ ] Admin view for audit trail

---

## 📌 Phase 7: Notification Templates

- [ ] Model: NotificationTemplate (type, name, subject, body)
- [ ] Allow placeholders like `{user_name}`, `{reset_link}`
- [ ] CRUD operations via admin panel

---

## 📌 Phase 8: System Settings

- [ ] General settings: Site name, maintenance mode
- [ ] Session config: max duration, buffer time
- [ ] Notification toggles: Enable/disable email/SMS
- [ ] Create a key-value pair model for dynamic settings
- [ ] APIs to update/fetch settings

---

## 🔒 Phase 9: Security & Rate Limiting

- [ ] Protect all endpoints with permissions and throttling
- [ ] Use `django-ratelimit` with Redis backend
- [ ] Block brute-force login attempts
- [ ] Restrict access to subscription-only features

---

## 🧪 Final Checklist

- [ ] All APIs are documented using drf-spectacular
- [ ] Postman collection exported and tested
- [ ] All tasks marked completed in this file
- [ ] Frontend tested against each API
- [ ] Admin dashboard is functional and secure

---

**Note:** This `Tasks.md` should be updated progressively. Task completion should be validated with real frontend integration and sample data.

