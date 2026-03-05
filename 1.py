# generators.py
import sys

def squares_upto(n):
    for i in range(1, n + 1):
        yield i * i

def evens_upto(n):
    for i in range(0, n + 1, 2):
        yield i

def div_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i

def squares(a, b):
    for x in range(a, b + 1):
        yield x * x

def countdown(n):
    for x in range(n, -1, -1):
        yield x

class Reverse:
    def __init__(self, s):
        self.s = s
        self.i = len(s) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < 0:
            raise StopIteration
        ch = self.s[self.i]
        self.i -= 1
        return ch

def primes_upto(n):
    if n < 2:
        return
        yield
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
        p += 1
    for i in range(2, n + 1):
        if sieve[i]:
            yield i

def powers_of_two(n):
    x = 1
    for _ in range(n + 1):
        yield x
        x *= 2

def cycle_k_times(lst, k):
    for _ in range(k):
        for item in lst:
            yield item

def _run():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    cmd = data[0].strip()

    if cmd == "squares_upto":
        n = int(data[1])
        sys.stdout.write("\n".join(str(x) for x in squares_upto(n)))

    elif cmd == "evens_upto":
        n = int(data[1])
        sys.stdout.write(",".join(str(x) for x in evens_upto(n)))

    elif cmd == "div_by_3_and_4":
        n = int(data[1])
        sys.stdout.write(" ".join(str(x) for x in div_by_3_and_4(n)))

    elif cmd == "squares_range":
        a, b = map(int, data[1].split())
        sys.stdout.write("\n".join(str(x) for x in squares(a, b)))

    elif cmd == "countdown":
        n = int(data[1])
        sys.stdout.write("\n".join(str(x) for x in countdown(n)))

    elif cmd == "reverse":
        s = data[1].rstrip("\n")
        sys.stdout.write("".join(ch for ch in Reverse(s)))

    elif cmd == "primes_upto":
        n = int(data[1])
        out = " ".join(str(x) for x in primes_upto(n))
        sys.stdout.write(out)

    elif cmd == "powers_of_two":
        n = int(data[1])
        sys.stdout.write(" ".join(str(x) for x in powers_of_two(n)))

    elif cmd == "cycle":
        lst = data[1].split()
        k = int(data[2])
        sys.stdout.write(" ".join(str(x) for x in cycle_k_times(lst, k)))

if name == "__main__":
    _run()
# dates.py
import sys
import re
from datetime import datetime, date, timedelta, timezone

def parse_utc_offset(s):
    m = re.fullmatch(r"UTC([+-])(\d{2}):(\d{2})", s.strip())
    sign = 1 if m.group(1) == "+" else -1
    hh = int(m.group(2))
    mm = int(m.group(3))
    return timezone(sign * timedelta(hours=hh, minutes=mm))

def parse_local_midnight(line):
    parts = line.strip().split()
    d = date.fromisoformat(parts[0])
    tz = parse_utc_offset(parts[1])
    return datetime(d.year, d.month, d.day, 0, 0, 0, tzinfo=tz).astimezone(timezone.utc)

def full_days_diff_midnights(line1, line2):
    t1 = parse_local_midnight(line1)
    t2 = parse_local_midnight(line2)
    delta = abs(t2 - t1)
    return int(delta.total_seconds() // 86400)

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def birthday_in_year(birth_month, birth_day, year):
    if birth_month == 2 and birth_day == 29 and not is_leap(year):
        return date(year, 2, 28)
    return date(year, birth_month, birth_day)

def days_until_next_birthday(birth_line, current_line):
    b_parts = birth_line.strip().split()
    c_parts = current_line.strip().split()
    b_date = date.fromisoformat(b_parts[0])
    c_date = date.fromisoformat(c_parts[0])
    b_tz = parse_utc_offset(b_parts[1])
    c_tz = parse_utc_offset(c_parts[1])

    current_utc = datetime(c_date.year, c_date.month, c_date.day, 0, 0, 0, tzinfo=c_tz).astimezone(timezone.utc)

    cand_year = c_date.year
    bday_local = birthday_in_year(b_date.month, b_date.day, cand_year)
    cand_utc = datetime(bday_local.year, bday_local.month, bday_local.day, 0, 0, 0, tzinfo=b_tz).astimezone(timezone.utc)

    if cand_utc < current_utc:
        cand_year += 1
        bday_local = birthday_in_year(b_date.month, b_date.day, cand_year)
        cand_utc = datetime(bday_local.year, bday_local.month, bday_local.day, 0, 0, 0, tzinfo=b_tz).astimezone(timezone.utc)

    delta = cand_utc - current_utc
    sec = int(delta.total_seconds())
    if sec <= 0:
        return 0
    return sec // 86400

def parse_moment(line):
    parts = line.strip().split()
    d = parts[0]
    tm = parts[1]
    tz = parse_utc_offset(parts[2])
    y, mo, da = map(int, d.split("-"))
    hh, mm, ss = map(int, tm.split(":"))
    return datetime(y, mo, da, hh, mm, ss, tzinfo=tz).astimezone(timezone.utc)

def event_duration_seconds(start_line, end_line):
    start = parse_moment(start_line)
    end = parse_moment(end_line)
    return int((end - start).total_seconds())

def _run():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    cmd = data[0].strip()

    if cmd == "days_diff":
        sys.stdout.write(str(full_days_diff_midnights(data[1], data[2])))

    elif cmd == "days_to_birthday":
        sys.stdout.write(str(days_until_next_birthday(data[1], data[2])))

    elif cmd == "event_duration":
        sys.stdout.write(str(event_duration_seconds(data[1], data[2])))

if name == "__main__":
    _run()
# math.py
import sys
import importlib

def classify_attribute(module_path, attr):
    try:
        mod = importlib.import_module(module_path)
    except Exception:
        return "MODULE_NOT_FOUND"
    if not hasattr(mod, attr):
        return "ATTRIBUTE_NOT_FOUND"
    val = getattr(mod, attr)
    return "CALLABLE" if callable(val) else "VALUE"

def scope_simulation(commands):
    g = 0
    n = 0
    inner_local = 0
    for kind, x in commands:
        if kind == "global":
            g += x
        elif kind == "nonlocal":
            n += x
        else:
            inner_local += x
    return g, n

def _run():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    cmd = data[0].strip()

    if cmd == "classify":
        q = int(data[1])
        out = []
        for i in range(q):
            mod, attr = data[2 + i].split()
            out.append(classify_attribute(mod, attr))
        sys.stdout.write("\n".join(out))

    elif cmd == "scopes":
        q = int(data[1])
        cmds = []
        for i in range(q):
            kind, x = data[2 + i].split()
            cmds.append((kind, int(x)))
        g, n = scope_simulation(cmds)
        sys.stdout.write(f"{g} {n}")

if name == "__main__":
    _run()
# json.py
import sys
import json
import re

def is_object(x):
    return isinstance(x, dict)

def apply_patch(source, patch):
    if not is_object(source) or not is_object(patch):
        return patch
    for k, v in patch.items():
        if v is None:
            if k in source:
                del source[k]
        elif k not in source:
            source[k] = v
        else:
            if is_object(source[k]) and is_object(v):
                apply_patch(source[k], v)
            else:
                source[k] = v
    return source

def diff_json(a, b):
    out = []

    def rec(x, y, path):
        if is_object(x) and is_object(y):
            keys = set(x.keys()) | set(y.keys())
            for k in keys:
                p = f"{path}.{k}" if path else k
                in_x = k in x
                in_y = k in y
                if in_x and in_y:
                    rec(x[k], y[k], p)
                elif in_x and not in_y:
                    out.append((p, x[k], "<missing>"))
                else:
                    out.append((p, "<missing>", y[k]))
        else:
            if x != y:
                out.append((path, x, y))

    rec(a, b, "")
    out.sort(key=lambda t: t[0])
    return out

_token_re = re.compile(r"""
    (?:
        \.([A-Za-z_][A-Za-z0-9_]*)
      | ^([A-Za-z_][A-Za-z0-9_]*)
      | \[(\d+)\]
    )
""", re.VERBOSE)

def resolve_query(value, query):
    pos = 0
    cur = value
    while pos < len(query):
        m = _token_re.match(query, pos)
        if not m:
            return None, False
        key1, key2, idx = m.group(1), m.group(2), m.group(3)
        if key1 or key2:
            key = key1 if key1 is not None else key2
            if not isinstance(cur, dict) or key not in cur:
                return None, False
            cur = cur[key]
        else:
            i = int(idx)
            if not isinstance(cur, list) or i < 0 or i >= len(cur):
                return None, False
            cur = cur[i]
        pos = m.end()
    return cur, True

def compact(v):
    if v == "<missing>":
        return "<missing>"
    return json.dumps(v, separators=(",", ":"))

def _run():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    cmd = data[0].strip()

    if cmd == "patch":
        src = json.loads(data[1])
        pat = json.loads(data[2])
        res = apply_patch(src, pat)
        sys.stdout.write(json.dumps(res, separators=(",", ":"), sort_keys=True))

    elif cmd == "diff":
        a = json.loads(data[1])
        b = json.loads(data[2])
        diffs = diff_json(a, b)
        if not diffs:
            sys.stdout.write("No differences")
        else:
            lines = []
            for p, old, new in diffs:
                lines.append(f"{p} : {compact(old)} -> {compact(new)}")
            sys.stdout.write("\n".join(lines))

    elif cmd == "query":
        obj = json.loads(data[1])
        q = int(data[2])
        out = []
        for i in range(q):
            val, ok = resolve_query(obj, data[3 + i].strip())
            if not ok:
                out.append("NOT_FOUND")
            else:
                out.append(json.dumps(val, separators=(",", ":")))
        sys.stdout.write("\n".join(out))

if name == "__main__":
    _run()