# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ADI Pod** (Artificial Developer Intelligence) is a technical podcast hosted by Shimin Zhang, Dan Lasky, and Rahul Yadav covering AI engineering, LLMs, and developer tooling. Website: adipod.ai. Contact: humans@adipod.ai.

This repository contains marketing plans and (when built) the podcast's static website.

## Current State

The project is in the planning phase. `marketing_plans/` contains strategy documents from multiple AI assistants covering SEO/GEO, content repurposing, and site architecture. No code has been written yet.

## Planned Architecture

The site scaffold plan (`marketing_plans/2026-04-10-site-scaffold-plan.md`) defines the target implementation:

- **Framework:** Astro 5.x with TypeScript and Zod content collections
- **Hosting:** Cloudflare Pages (free tier)
- **Content source:** Markdown files from podcast transcripts (located in a separate `workspace/.pi/skills/podcast-transcripts/` directory)
- **Content types:** Episodes, glossary terms, blog posts, topic pillar pages, segment hub pages, host bio pages
- **Schema markup:** JSON-LD (PodcastSeries, PodcastEpisode, Article, DefinedTerm, FAQPage, Person) baked into Astro layouts
- **Site root:** `site/` subdirectory

## Key Context

- The podcast has ~20 episodes with 200K+ words of transcripts — the primary content asset
- Target audience: working software engineers navigating AI tooling
- Brand voice: "AI news without the LinkedIn cringe" — technically rigorous, anti-hype, practitioner-first
- Operator is solo (Shimin) with 3-5 hrs/week for marketing; agent-driven content generation is central to the strategy
- The SEO/GEO plan (`marketing_plans/2026-04-10-agent-powered-seo-geo-plan.md`) is the canonical strategy document
