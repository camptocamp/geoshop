# Part 2 - Create and validate an account

Before attempting to order a product, you need to have a non-admin user account.

### Create an account

To create a new user account, you can use the front-end just like any standard client would.

1. Navigate to https://localhost/en
2. Click on the user icon at the top right and select ***Sign Up***.
3. Fill in the required information and choose a strong password.
4. Once submitted, the user account will be pending validation. An email will be sent to the admins requesting validation, and another email will be sent to the new user informing them that their account is pending validation.

:::info
At this point in the tutorial, emails are not actually being sent because we haven't configured an SMTP server. Instead, they are logged in the API Docker service logs.
:::

### Validate an account

1. Go back to the admin interface at https://localhost/api/admin.
2. Log in as admin:
    * Username: admin
    * Password: Test1234
3. Click on ***Users*** and then select the username you just created.
4. Check the ***Active*** checkbox under the ***PERMISSIONS*** section.
5. Scroll down and click the <Badge type="tip" text="Send confirmation email to client" /> button.

Congratulations! You've successfully created a customer account. To learn more about users, please refer to the [documentation about users](./../documentation/users).