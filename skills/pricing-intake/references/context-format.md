# Context file format

`.pricing/context.md` stays plain Markdown. Keep this light structure so other skills, and later imports into other projects, can tell what applies.

## Header

```text
# Pricing context: <company>
Scope: <business units, regions or products covered>
Last updated: <YYYY-MM-DD>
```

- Write `not stated` for a company or scope you have not been told, and ask the user to fill it in.
- A missing header field never blocks saving a confirmed fact.

## Facts

- Group facts under whatever headings suit the business. Do not add empty headings.
- Write each fact as one bullet ending with its scope, confirmation date and source.
- A fact with no scope applies company-wide.
- An exception names its rule and the customers or products it covers.

```text
- Gross margin = (net sales − standard COGS) / net sales. [scope: all regions; confirmed 2026-10-11; finance policy]
```

## Change log

End the file with a `## Change log` section. Each intake that changes the file appends one line: the date, and which facts were added, replaced or removed.
