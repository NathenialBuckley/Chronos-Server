# Deployment Checklist

Use this checklist to ensure a smooth deployment process.

## Pre-Deployment

### Code Preparation
- [ ] All tests are passing
- [ ] Code is committed to version control
- [ ] `.env` is in `.gitignore` (never commit secrets)
- [ ] Dependencies are up to date in `Pipfile` or `requirements-prod.txt`

### Settings Configuration
- [ ] `DJANGO_ENV=production` environment variable is set
- [ ] `DEBUG=False` in production settings
- [ ] Generated a strong `SECRET_KEY` for production
- [ ] `ALLOWED_HOSTS` configured with production domains
- [ ] `CORS_ALLOWED_ORIGINS` configured with frontend URLs

### Database
- [ ] Production database created (PostgreSQL recommended)
- [ ] Database credentials are secure
- [ ] `DATABASE_URL` environment variable is set
- [ ] Migrations have been created and tested locally

### Security
- [ ] All security settings enabled in `settings_prod.py`
- [ ] SSL/HTTPS will be enabled
- [ ] Strong passwords for database and admin accounts
- [ ] Secrets are stored as environment variables, not in code

## Deployment Steps

### Initial Setup
- [ ] Production server or cloud platform configured
- [ ] Environment variables set in production environment
- [ ] Static file storage configured
- [ ] Media file storage configured

### Database Migration
- [ ] Run `python manage.py migrate`
- [ ] Create superuser with `python manage.py createsuperuser`
- [ ] (Optional) Load seed data

### Static Files
- [ ] Run `python manage.py collectstatic --noinput`
- [ ] Verify static files are being served correctly
- [ ] Test admin panel loads with styles

### Application Deployment
- [ ] Application code deployed to production
- [ ] Gunicorn configured and running
- [ ] Web server (Nginx/Apache) configured (if self-hosted)
- [ ] Application starts without errors

## Post-Deployment

### Testing
- [ ] Test home/root endpoint responds
- [ ] Test `/admin/` loads correctly
- [ ] Test registration endpoint: `POST /register/`
- [ ] Test login endpoint: `POST /login/`
- [ ] Test authenticated endpoint: `GET /watches/` with token
- [ ] Test CORS by making requests from frontend
- [ ] Test database connections
- [ ] Test file uploads to media directory

### Monitoring
- [ ] Set up logging
- [ ] Configure error monitoring (Sentry, etc.)
- [ ] Set up uptime monitoring
- [ ] Configure database backups

### Documentation
- [ ] Update frontend with production API URL
- [ ] Document deployment process
- [ ] Share API documentation with team
- [ ] Update README with production URL

## Ongoing Maintenance

### Regular Tasks
- [ ] Monitor application logs
- [ ] Monitor database performance
- [ ] Review error reports
- [ ] Apply security updates

### Backup Strategy
- [ ] Database backup schedule configured
- [ ] Backup restoration process tested
- [ ] Media files backup configured

### Scaling Preparation
- [ ] Monitor resource usage (CPU, memory, disk)
- [ ] Identify performance bottlenecks
- [ ] Plan for horizontal scaling if needed

## Environment Variables Verification

Use this section to track which environment variables are set:

```bash
# Check all required environment variables are set
heroku config  # For Heroku

# Or for self-hosted, create a verification script
cat > check_env.sh << 'EOF'
#!/bin/bash
required_vars=("DJANGO_ENV" "SECRET_KEY" "ALLOWED_HOSTS" "CORS_ALLOWED_ORIGINS" "DATABASE_URL")
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ $var is not set"
    else
        echo "✅ $var is set"
    fi
done
EOF
chmod +x check_env.sh
./check_env.sh
```

## Rollback Plan

In case of deployment issues:

1. **Identify the issue**
   - Check logs: `heroku logs --tail` or `journalctl -u chronos -f`
   - Check error messages

2. **Quick fixes**
   - Restart application: `heroku restart` or `systemctl restart chronos`
   - Verify environment variables
   - Check database connectivity

3. **Full rollback**
   - Revert to previous git commit
   - Redeploy previous version
   - Restore database from backup if needed

4. **Post-rollback**
   - Investigate root cause
   - Test fix in staging environment
   - Redeploy when ready

## Success Criteria

Your deployment is successful when:

- [ ] All API endpoints respond correctly
- [ ] Frontend can authenticate and make requests
- [ ] No errors in application logs
- [ ] Database queries execute successfully
- [ ] Static and media files load correctly
- [ ] HTTPS is working (if enabled)
- [ ] Application is accessible from production domain

## Support Contacts

- **Platform Support**: [Platform documentation/support]
- **Database Issues**: [Database admin contact]
- **DNS/Domain Issues**: [Domain registrar support]
- **Development Team**: [Team contact information]

---

**Last Updated**: [Date]
**Deployed By**: [Name]
**Deployment Date**: [Date]
**Version**: [Git commit hash or version number]
