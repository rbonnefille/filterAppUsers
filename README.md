# Filter App Users

This project contains scripts to filter appUsers based on the CSV file header `numberOfConversations`

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

Import csv file with the following columns:

| appUserId                | userId         | lastSeen                 | createdAt                | numberOfConversations | verifiedEmail              |
| ------------------------ | -------------- | ------------------------ | ------------------------ | --------------------- | -------------------------- |
| 658427da1c9607d863cab82d | dwight-schrute | 2025-02-17T08:28:28.768Z | 2023-12-21T11:56:10.910Z | 127                   | dwight-schrute@example.com |

To filter users, run the following command:

```bash
python filter_users.py
```
