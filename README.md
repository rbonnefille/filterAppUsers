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

| appUserId | userId | lastSeen | createdAt | numberOfConversations | verifiedEmail |
| --------- | ------ | -------- | --------- | --------------------- | ------------- |
|           |        |          |           |                       |               |

To filter users, run the following command:

```bash
python filter_users.py
```
