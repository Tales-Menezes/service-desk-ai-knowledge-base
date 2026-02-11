# Service Desk AI Knowledge Base

## Overview
An AI-powered, client-aware knowledge base designed to help service desk
engineers quickly retrieve accurate information from internal documentation.

The system uses Retrieval-Augmented Generation (RAG) to ensure that answers
are grounded in official, client-specific knowledge base documents.

## Problem Statement
Service desk engineers often lose time searching through PDFs, Word documents,
and internal portals to find client-specific procedures such as leaver
processes, access approvals, or printer installations.

This project solves that problem by combining semantic search and AI-driven
question answering in a secure, enterprise-ready system.

## Key Features
- Azure AD (Entra ID) authentication and role-based access
- Search interface with client-aware filtering
- Supports PDF, DOCX, TXT, and Markdown (.md) documents
- Mock retrival backend for local development and testing
- Client-aware document ingestion
- Semantic and vector search using Azure Cognitive Search
- AI-powered answers using Azure OpenAI (RAG)
- Audit logging of searches and document access
- Infrastructure as Code using Terraform

## Architecture
(Architecture diagram coming soon)

## Local Development Mode
For local development, the application supports a mock search backend
that simulates Azure Cognitive Search. This allows ingestion and retrieval
to be tested without requiring Azure resources.

The backend can be switched via environment configuration.

## Tech Stack
- Python / Flask
- Azure OpenAI
- Azure Cognitive Search
- Azure Blob Storage
- Azure SQL Database
- Terraform

## Project Status
🚧 Work in progress – actively building core features.