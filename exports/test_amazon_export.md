# Quick Test: Amazon KDP Export

## Testing the Compilation Tool for Publication

Let's run a clean export specifically for Amazon KDP submission:

```bash
python tools\compile_book.py --book 1 --format txt --clean-export --output "fragmented_city_amazon_kdp"
```

This will create a clean version without experimental artifacts for traditional readers while preserving the core narrative.