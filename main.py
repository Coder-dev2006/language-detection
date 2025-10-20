import argparse
import json
import csv
from langdetect import detect, detect_langs, DetectorFactory, LangDetectException
import sys

# make langdetect deterministic (optional)
DetectorFactory.seed = 0

# try to import pycountry for nicer language names
try:
    import pycountry
except Exception:
    pycountry = None

def iso_to_name(code):
    if not pycountry:
        return code
    try:
        lang = pycountry.languages.get(alpha_2=code)
        # pycountry may not have alpha_2 for all codes (e.g., 'zh-cn'), try lookup by alpha_3 or name fallback
        if not lang:
            lang = pycountry.languages.get(alpha_3=code)
        return lang.name if lang and hasattr(lang, "name") else code
    except Exception:
        return code

def analyze_text(text, top_n=3):
    text = text.strip()
    if not text:
        return {"text": text, "error": "empty"}
    try:
        primary = detect(text)
        langs = detect_langs(text)
        # langs is like [en:0.999995, fr:0.000004]
        probs = []
        for i, item in enumerate(langs):
            if i >= top_n:
                break
            code = item.lang
            prob = round(item.prob, 6)
            probs.append({"code": code, "name": iso_to_name(code), "prob": prob})
        return {"text": text, "language": primary, "language_name": iso_to_name(primary), "probs": probs}
    except LangDetectException as e:
        return {"text": text, "error": str(e)}

def process_lines(lines, top_n=3, show_progress=False):
    results = []
    total = len(lines)
    for i, line in enumerate(lines, start=1):
        if show_progress and total:
            print(f"\rProcessing {i}/{total}", end="", flush=True)
        res = analyze_text(line, top_n=top_n)
        results.append(res)
    if show_progress:
        print()
    return results

def write_csv(results, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "language_code", "language_name", "top_probs"])
        for r in results:
            if r.get("error"):
                writer.writerow([r.get("text"), "", "", f"ERROR: {r['error']}"])
            else:
                probs_str = ";".join(f"{p['code']}:{p['prob']}" for p in r["probs"])
                writer.writerow([r["text"], r["language"], r["language_name"], probs_str])

def write_json(results, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

def main():
    ap = argparse.ArgumentParser(description="Enhanced language detection CLI (langdetect)")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--text", help="Text to detect (quote it on shell)")
    group.add_argument("-f", "--file", help="Path to a text file (each line will be detected as separate sample)")
    ap.add_argument("--top", type=int, default=3, help="How many probable languages to show (default 3)")
    ap.add_argument("--json", help="Write results to JSON file")
    ap.add_argument("--csv", help="Write summarized results to CSV file")
    ap.add_argument("-v", "--verbose", action="store_true", help="Verbose / progress")
    args = ap.parse_args()

    # prepare input lines
    lines = []
    if args.text:
        lines = [args.text]
    else:
        try:
            with open(args.file, "r", encoding="utf-8", errors="replace") as fh:
                # discard empty lines by default; keep if you want
                lines = [ln.rstrip("\n") for ln in fh if ln.strip() != ""]
        except Exception as e:
            print(f"Error opening file: {e}", file=sys.stderr)
            sys.exit(2)

    results = process_lines(lines, top_n=args.top, show_progress=args.verbose)

    # print to console nicely
    for r in results:
        if r.get("error"):
            print(f"[ERROR] {r['error']} — text: {r['text']!r}")
        else:
            probs = ", ".join(f"{p['code']}({p['prob']})" for p in r["probs"])
            print(f"Detected: {r['language']} / {r['language_name']}  — top: {probs}")
            if args.verbose:
                print(f"  text: {r['text']!r}")

    if args.csv:
        try:
            write_csv(results, args.csv)
            print(f"Saved CSV -> {args.csv}")
        except Exception as e:
            print(f"Could not write CSV: {e}", file=sys.stderr)

    if args.json:
        try:
            write_json(results, args.json)
            print(f"Saved JSON -> {args.json}")
        except Exception as e:
            print(f"Could not write JSON: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
