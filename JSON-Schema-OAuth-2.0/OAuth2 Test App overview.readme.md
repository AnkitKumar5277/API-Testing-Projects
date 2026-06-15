# GitHub OAuth 2.0 Authentication Using Postman

## Overview

OAuth 2.0 is an authorization framework that allows applications to access user data without requiring the user's password.

In this tutorial, you'll learn how to:

* Register an OAuth App on GitHub
* Configure OAuth 2.0 in Postman
* Generate an Access Token
* Use the token to access GitHub APIs

---

# Understanding OAuth 2.0

Think of OAuth 2.0 like this:

> You want to access your GitHub profile using another application (such as Postman) without sharing your GitHub password. GitHub verifies your identity and provides a temporary access token that Postman can use to access your data.

## OAuth 2.0 Roles

| Role                 | Example             |
| -------------------- | ------------------- |
| Resource Owner       | You (GitHub User)   |
| Client               | Postman             |
| Authorization Server | GitHub Login System |
| Resource Server      | GitHub API          |

---

# Step 1: Register an OAuth App on GitHub

First, create an OAuth application in GitHub.

## Navigate To

https://github.com/settings/developers

## Create a New OAuth App

Click **New OAuth App** and fill in the following details:

| Field                      | Value                              |
| -------------------------- | ---------------------------------- |
| Application Name           | OAuth2 Test App                    |
| Homepage URL               | https://example.com                |
| Authorization Callback URL | https://oauth.pstmn.io/v1/callback |

Click **Register Application**.

## Save Credentials

GitHub will generate:

* **Client ID** → Application Identifier
* **Client Secret** → Application Password

Store these securely because they will be used in Postman.

---

# Step 2: Configure OAuth 2.0 in Postman

1. Open Postman.
2. Create a new request.
3. Name it **GitHub OAuth2 Test**.
4. Open the **Authorization** tab.
5. Select **OAuth 2.0** from the Type dropdown.
6. Click **Get New Access Token**.

---

# Step 3: Configure OAuth Details

Enter the following values:

| Field                 | Value                                       |
| --------------------- | ------------------------------------------- |
| Token Name            | GitHub OAuth                                |
| Grant Type            | Authorization Code                          |
| Callback URL          | https://oauth.pstmn.io/v1/callback          |
| Auth URL              | https://github.com/login/oauth/authorize    |
| Access Token URL      | https://github.com/login/oauth/access_token |
| Client ID             | Your GitHub Client ID                       |
| Client Secret         | Your GitHub Client Secret                   |
| Scope                 | read:user                                   |
| Client Authentication | Send as Basic Auth Header                   |

Click **Get New Access Token**.

---

# Step 4: Authorize the Application

1. Postman opens a browser window.
2. Log in to GitHub if required.
3. GitHub asks for permission to access your account.
4. Click **Authorize**.
5. GitHub redirects back to Postman.
6. Postman displays the generated Access Token.
7. Click **Use Token**.

The token is now attached to your requests.

---

# Step 5: Call GitHub API Using the Access Token

Create a new request:

### Request

```http
GET https://api.github.com/user
```

### Authorization

Type:

```text
Bearer Token
```

Token:

```text
<Access Token Generated Above>
```

Click **Send**.

---

# Expected Response

```json
{
  "login": "yourusername",
  "id": 123456,
  "node_id": "MDQ6VXNlcjE2ODk4NTI=",
  "avatar_url": "https://avatars.githubusercontent.com/u/123456?v=4",
  "url": "https://api.github.com/users/yourusername"
}
```

This response contains your GitHub profile information retrieved using OAuth 2.0 authorization.

---

# OAuth 2.0 Flow Explained

| Step | Action          | What Happens Behind the Scenes                     |
| ---- | --------------- | -------------------------------------------------- |
| 1    | Click Get Token | Postman redirects to GitHub Login                  |
| 2    | Login & Consent | GitHub verifies identity and asks for permission   |
| 3    | Authorize       | GitHub sends an Authorization Code to Postman      |
| 4    | Exchange Code   | Postman sends the code and Client Secret to GitHub |
| 5    | Receive Token   | GitHub returns an Access Token                     |
| 6    | API Request     | Postman sends the token to GitHub API              |
| 7    | Response        | GitHub validates the token and returns user data   |

---

# Sequence Diagram

```text
User
  |
  | Click Get Token
  v
Postman
  |
  | Redirect
  v
GitHub Authorization Server
  |
  | Login + Consent
  v
GitHub
  |
  | Authorization Code
  v
Postman
  |
  | Exchange Code + Client Secret
  v
GitHub Token Endpoint
  |
  | Access Token
  v
Postman
  |
  | GET /user
  v
GitHub API
  |
  | User Profile Data
  v
Postman
```

---

# Conclusion

You have successfully:

* Created a GitHub OAuth Application
* Configured OAuth 2.0 Authorization Code Flow in Postman
* Generated an Access Token
* Accessed GitHub APIs securely without using your password

This is one of the most commonly used OAuth 2.0 flows in modern web applications and APIs.
