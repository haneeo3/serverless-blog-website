# 📝 Serverless Blog Website — AWS Cloud Project

A fully serverless **Blog Website** built using:
**AWS Lambda (Python), API Gateway, DynamoDB, and S3.**

Users can create posts with **title, content, and image uploads**, and the data is stored in DynamoDB while images go to S3.

This is my **4th Cloud Project** in my Solo Leveling Cloud Journey.

---

## 🚀 Project Overview

This project is a lightweight serverless blogging backend + frontend system.

It includes:

* A **static frontend** built with HTML, CSS, JavaScript
* Backend built with **AWS Lambda in Python**
* Blog post storage in DynamoDB
* Image uploading to Amazon S3
* API routing via API Gateway
* Complete serverless architecture (no servers to manage)

---

## 🏗️ Architecture

```
Frontend (HTML + JS)
        |
        v
   API Gateway (REST)
        |
        v
+------------------------+
| Lambda Functions (Py) |
+------------------------+
   |               |
   v               v
DynamoDB        S3 Bucket
(Post data)   (Image uploads)
```

---

## ✨ Features

✓ Upload blog images
✓ Submit blog post (title + content + imageUrl)
✓ Store blog post in DynamoDB
✓ Fetch all blog posts
✓ Fully serverless backend
✓ Works with any static frontend
✓ Minimal, cheap, and scalable

---

## 📁 Project Structure (Accurate)

```
serverless-blog-website/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── backend/
    ├── create_post.py         # Lambda: Save post to DynamoDB
    ├── get_posts.py           # Lambda: Fetch all posts
    ├── upload_image.py        # Lambda: Upload to S3 (if using Lambda upload)
    └── utils/                 # (optional helpers)
```

---

## 🛠️ Tech Stack

| Layer        | Technology                |
| ------------ | ------------------------- |
| Frontend     | HTML, CSS, JavaScript     |
| Backend      | AWS Lambda (Python 3.9+)  |
| API          | Amazon API Gateway (REST) |
| Database     | Amazon DynamoDB           |
| Storage      | Amazon S3                 |
| Auth         | None (public API for now) |
| Architecture | Serverless                |

---

## 📦 DynamoDB Table — `BlogPosts`

Partition key: **postId (String)**

| Field     | Type   | Description              |
| --------- | ------ | ------------------------ |
| postId    | String | UUID generated in Lambda |
| title     | String | Blog title               |
| content   | String | Blog content             |
| imageUrl  | String | S3 or frontend URL       |
| createdAt | String | ISO timestamp (UTC)      |

---

## 🔥 API Endpoints

All requests go through **API Gateway REST API** using **Lambda Proxy Integration**.

| Method | Path            | Description                   | Lambda Function   |
| ------ | --------------- | ----------------------------- | ----------------- |
| POST   | `/create-post`  | Create a new post             | `create_post.py`  |
| GET    | `/get-posts`    | Fetch all blog posts          | `get_posts.py`    |
| POST   | `/upload-image` | Upload image to S3 (optional) | `upload_image.py` |

---

## 🧠 Lambda (Python) — How It Works

### ✔️ `create_post.py`

* Receives body via API Gateway proxy → `event["body"]`
* Parses title, content, imageUrl
* Generates UUID
* Inserts item into DynamoDB
* Returns JSON response

### ✔️ `get_posts.py`

* Scans DynamoDB table
* Returns all items

### ✔️ `upload_image.py` (if used)

* Receives base64 or form upload
* Puts object in S3
* Returns file URL

---

## 🔐 IAM Permissions (What You *Actually* Used)

The Lambda execution role must allow:

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:PutItem",
    "dynamodb:Scan",
    "dynamodb:UpdateItem",
    "dynamodb:DeleteItem",
    "s3:PutObject",
    "s3:GetObject"
  ],
  "Resource": "*"
}
```

---

## ⚙️ How to Deploy (Accurate)

### 1️⃣ Deploy the Backend

* Create Lambda functions
* Paste Python code
* Connect each endpoint to each Lambda
* Enable Lambda Proxy Integration
* Deploy API to a stage (e.g., `/prod`)

### 2️⃣ Create DynamoDB Table

Name: `BlogPosts`
Partition key: `postId` (String)

### 3️⃣ Create S3 Bucket

* Enable public access or signed URLs
* Store uploaded images

### 4️⃣ Deploy Frontend

Upload your HTML/CSS/JS to:

* AWS S3 static website hosting
  **or**
* GitHub Pages
  **or**
* Any static hosting


---

## 💡 Why I Built This

I built this to practice:

* Serverless applications
* API Gateway + Lambda Proxy
* DynamoDB NoSQL design
* S3 object upload architecture
* Python Lambda API handling
* Cloud project structuring

And to create a real-world backend I can show recruiters.

---

## 📬 Contact

* **Portfolio:** [https://haneeo3.github.io/olajobihaneef](https://haneeo3.github.io/olajobihaneef)
* **GitHub:** [https://github.com/haneeo3](https://github.com/haneeo3)
* **LinkedIn:** [https://linkedin.com/in/haneef-olajobi](https://linkedin.com/in/haneef-olajobi)

---

