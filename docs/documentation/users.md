# Users and Identities

In GeoShop, user management is based on standard Django user accounts, which include basic information and permissions. It is essential to check the ***Active*** checkbox; otherwise, the user will be unable to log in.

Each user must have an ***Identity***, which is automatically created upon registration. Identities store additional information that is not directly related to authentication and permissions, such as address, date of birth, and more.

While you cannot create an user without an associated Identity, you can create an Identity independently without linking it to a user. 

Identities, whether associated with users or not, can be linked to Metadata as contact persons. To do this, you must obtain consent from the individual. Once you have consent, you can check the ***is_public*** checkbox on the Identity, allowing it to be used as a contact person.

## Subscription

The ***Subscribed*** checkbox is meant to manage subscriptions. A subscribed user will be able to order for free every product marked as ***free_when_subscribed***.
