#!/usr/bin/env python3
"""
Build script that converts markdown posts to HTML pages.
Reads from _posts/ directory and outputs to posts/ directory.
Also updates index.html with the posts list.
"""

import re
import markdown
from pathlib import Path
from datetime import datetime

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown file."""
    if not content.startswith('---'):
        return {}, content

    # Find the second --- delimiter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter_text = match.group(1)
    body = match.group(2)

    # Parse simple YAML (title, date, description)
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()

    return metadata, body

def get_slug_from_filename(filename):
    """Convert filename to URL slug.
    e.g., 2025-11-05-first-post.md -> first-post"""
    base = filename.replace('.md', '')
    # Remove date prefix (YYYY-MM-DD-)
    parts = base.split('-', 3)
    if len(parts) >= 4:
        return '-'.join(parts[3:])
    return base

def generate_html_file(title, date, body_html, slug):
    """Generate full HTML file for a post."""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Jack Wittmayer</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="container">
        <nav class="navbar">
            <h1><a href="/">Jack Wittmayer</a></h1>
            <ul>
                <li><a href="/about.html">About</a></li>
            </ul>
        </nav>

        <main>
            <article class="blog-post">
                <h1>{title}</h1>
                <p class="post-date">{date}</p>

                {body_html}
            </article>
        </main>

        <footer>
            <p>© 2025 Jack Wittmayer</p>
        </footer>
    </div>
</body>
</html>"""
    return html_template

def generate_latest_post_html(post):
    """Generate HTML for the latest post section."""
    return f"""<article class="post">
                    <h3><a href="/posts/{post['slug']}.html">{post['title']}</a></h3>
                    <p class="post-date">{post['date']}</p>
                    <p>{post['description']}</p>
                    <a href="/posts/{post['slug']}.html" class="read-more">Read more →</a>
                </article>"""

def generate_all_posts_html(posts_list):
    """Generate HTML for all posts list."""
    items = []
    for post in posts_list:
        items.append(f"""<li>
                        <a href="/posts/{post['slug']}.html">{post['title']}</a>
                        <span class="post-list-date">{post['date']}</span>
                    </li>""")
    return f"""<ul class="posts-list">
                {chr(10).join(items)}
            </ul>"""

def generate_posts_json(posts_list):
    """Generate a JSON file with posts metadata."""
    import json

    posts_json = json.dumps(posts_list, indent=2)

    json_file = Path('posts.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(posts_json)

    print('✓ Generated posts.json with posts metadata')

def build_posts():
    """Build all posts from markdown to HTML."""
    posts_dir = Path('_posts')
    output_dir = Path('posts')

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Collect all posts for the index
    posts_list = []

    # Process each markdown file
    for md_file in sorted(posts_dir.glob('*.md'), reverse=True):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter and body
        metadata, body = parse_frontmatter(content)

        title = metadata.get('title', 'Untitled')
        date = metadata.get('date', '')
        description = metadata.get('description', '')

        # Convert markdown body to HTML
        body_html = markdown.markdown(body)

        # Get slug for filename
        slug = get_slug_from_filename(md_file.name)

        # Generate HTML file
        html_content = generate_html_file(title, date, body_html, slug)

        # Write HTML file
        output_file = output_dir / f'{slug}.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f'✓ Built {md_file.name} -> {output_file.name}')

        # Store metadata for index generation
        posts_list.append({
            'title': title,
            'date': date,
            'slug': slug,
            'description': description
        })

    # Generate posts.json for dynamic loading
    if posts_list:
        generate_posts_json(posts_list)

    print(f'\n✓ Successfully built {len(posts_list)} posts!')
    return posts_list

if __name__ == '__main__':
    build_posts()
