# Student Utility Bill Organizer

A personal assistant application designed to help students manage and organize their utility bills efficiently.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Student Utility Bill Organizer is a comprehensive solution for students to track, manage, and optimize their utility expenses. This application provides a user-friendly interface across web and mobile platforms, leveraging AI to offer personalized insights and recommendations.

## Features

- Bill tracking and organization
- Expense categorization
- Payment reminders
- Roommate bill splitting
- AI-powered cost-saving suggestions
- Usage analytics and reports
- Multi-platform support (Web and Mobile)

## Tech Stack

This project utilizes a modern and robust tech stack:

### Core

- **Turborepo**: Monorepo management
- **Expo**: Mobile app development
- **Next.js**: Web application framework
- **Hono**: Web framework for backend services
- **FastAPI**: Backend for AI functionality
- **Poetry**: Python package management

### Styling

- **TailwindCSS**: Utility-first CSS framework
- **Shadcn**: UI component library

### Authentication

- **Clerk**: User authentication and management

### AI and Data Processing

- **Langchain**: Large language model integration
- **Firecrawl**: Web scraping and data extraction
- **CrewAI**: AI agent orchestration

### Analytics and Monitoring

- **Posthog**: Product analytics
- **OpenPanel**: Data visualization and reporting
- **Sentry**: Error tracking and performance monitoring

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```
   bun install
   ```
3. Set up environment variables (refer to `.env.example`)
4. Run the development server:
   ```
   bun run dev
   ```

## Project Structure

```
student-utility-organizer/
├── apps/
│   ├── expo/    # Mobile application
│   ├── web/     # Next.js web application
│   └── api/     # FastAPI backend
├── packages/    # Shared packages
├── services/    # Microservices
└── tools/       # Development tools
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the [MIT License](LICENSE).
