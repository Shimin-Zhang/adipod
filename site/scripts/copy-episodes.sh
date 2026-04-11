#!/usr/bin/env bash
set -euo pipefail

TRANSCRIPT_DIR="/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts"
SUMMARY_DIR="/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/summaries"
OUTPUT_DIR="/home/shimin/projects/adi_pod/episodes"

mkdir -p "$OUTPUT_DIR"

for transcript in "$TRANSCRIPT_DIR"/ep-*.md; do
  filename=$(basename "$transcript")
  ep_num=$(echo "$filename" | sed 's/ep-\(.*\)\.md/\1/')
  summary_file="$SUMMARY_DIR/ep-${ep_num}-summary.md"

  # Read frontmatter fields from transcript
  title=$(sed -n 's/^title: "\(.*\)"/\1/p' "$transcript")
  date=$(sed -n 's/^date: "\(.*\)"/\1/p' "$transcript")

  # Generate slug from title: lowercase, replace non-alphanumeric with hyphens, trim
  slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')
  slug="${ep_num}-${slug}"

  # Extract summary overview (the line after **Overview:**)
  description=""
  if [ -f "$summary_file" ]; then
    description=$(sed -n 's/^\*\*Overview:\*\* //p' "$summary_file")
  fi

  # Extract keywords from summary
  keywords=""
  if [ -f "$summary_file" ]; then
    keywords=$(sed -n 's/^\*\*Keywords:\*\* //p' "$summary_file")
  fi

  # Get transcript body (everything after frontmatter closing ---)
  body=$(awk 'BEGIN{c=0} /^---$/{c++; if(c==2){found=1; next}} found{print}' "$transcript")

  # Get summary body (everything after frontmatter closing ---)
  summary_body=""
  if [ -f "$summary_file" ]; then
    summary_body=$(awk 'BEGIN{c=0} /^---$/{c++; if(c==2){found=1; next}} found{print}' "$summary_file")
  fi

  # Write combined episode file
  cat > "$OUTPUT_DIR/$filename" <<FRONTMATTER
---
episode: "$ep_num"
title: "$title"
date: "$date"
slug: "$slug"
description: "$(echo "$description" | sed 's/"/\\"/g')"
keywords: "$keywords"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: ""
---

$summary_body

---

## Full Transcript

$body
FRONTMATTER

  echo "Processed ep-${ep_num}: $title"
done

echo "Done. $(ls "$OUTPUT_DIR"/ep-*.md | wc -l) episodes copied."
