# Developer Snapshot API

![API Status](https://img.shields.io/badge/status-in%20development-yellow)
![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-0.1.0-lightgrey)

An intelligent API that analyzes a developer's GitHub profile to provide qualitative insights about their skills, impact, and collaboration style. This project aims to transform raw GitHub data into a meaningful developer "snapshot".

## The Problem

Recruiters and tech leads often spend hours manually analyzing GitHub profiles to understand a candidate's true capabilities. A contribution graph shows activity, but it doesn't tell the whole story. Key questions remain unanswered:

-   What are the developer's actual, demonstrated skills, beyond what's listed on their resume?
-   Which of their contributions had a real impact?
-   What is their collaboration style like in a team environment?

The Developer Snapshot API was created to answer these questions, providing deep, qualitative insights programmatically.

## Features

-   **Intelligent Skill Inference:** Analyzes repository code to identify specific skills and technologies (e.g., "REST API design with Express.js" instead of just "JavaScript").
-   **Impactful Contribution Analysis:** Pinpoints the most significant pull requests and contributions in third-party projects.
-   **Collaboration Style Profiling:** Assesses interactions in issues and pull requests to determine a collaboration archetype (e.g., "Detailed Reviewer," "Responsive Mentor").
-   **Project Archetype Classification:** Categorizes a developer's personal projects to showcase their areas of interest (e.g., "CLI Tools," "Frontend Libraries," "IoT Projects").

## API Usage

The API is simple and straightforward. Make a GET request to the main endpoint with a valid GitHub username.

### Get Developer Snapshot

`GET /v1/user/{username}/snapshot`

#### Example Request

```bash
curl -X GET [https://api.yourdomain.com/v1/user/octocat/snapshot](https://api.yourdomain.com/v1/user/octocat/snapshot)