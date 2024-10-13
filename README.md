# Intor - Student Utility Bill Organizer

Intor is a powerful personal assistant designed to help students efficiently manage and organize their utility bills. This CRM-style application leverages cutting-edge technologies to provide a seamless experience across mobile and web platforms.

## Tech Stack

### Frontend

- **Mobile**: Expo
- **Web**: Next.js
- **Styling**:
  - TailwindCSS
  - Shadcn

### Backend

- **Web Framework**: Hono
- **AI Functionality**: FastAPI
- **Authentication**: Clerk

### AI Technologies

- Langchain
- Firecrawl
- CrewAI

### Analytics

- Posthog
- OpenPanel

### Application Monitoring

- Sentry

### Package Managers

- Turborepo (Monorepo management)
- Bun (JavaScript runtime and package manager)
- Poetry (Python package manager)

## Architecture

Intor is built using a monorepo structure managed by Turborepo, with the following main components:

1. **Mobile App (Expo)**

   - Provides a native mobile experience for iOS and Android users

2. **Web App (Next.js)**

   - Offers a responsive web interface for desktop and mobile browsers

3. **Backend Services**

   - Hono: Handles non-AI related backend functionality
   - FastAPI: Manages AI-powered features and integrations

4. **Shared Components**
   - Common UI components and utilities shared between mobile and web apps

## Key Features

- Intuitive bill organization and tracking
- AI-powered insights and recommendations
- Cross-platform synchronization
- Secure authentication and data protection
- Real-time analytics and reporting

## Getting Started

1. Clone the repository
2. Install dependencies using Bun
3. Set up environment variables
4. Run the development servers for mobile, web, and backend services

Detailed setup instructions can be found in the `CONTRIBUTING.md` file.

## Contributing

We welcome contributions from the community! Please read our `CONTRIBUTING.md` file for guidelines on how to submit pull requests, report issues, and suggest improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support

For any questions or support, please open an issue in the GitHub repository or contact our support team at support@intor.app.

---

Intor - Simplifying utility management for students, one bill at a time.
