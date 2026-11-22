# advent-of-code

Run commands from the repository root with `just` and `uv` installed. On Windows,
the recipes use PowerShell.

```powershell
just                  # List available commands
just test 2025 1      # Run both parts with sample input
just run 2025 1       # Run both parts with actual puzzle input
```

Replace the year and day as needed. Input files belong in `data/<year>/`:
`test_input_01.txt` for samples and `input_01.txt` for actual input (with a
two-digit day). The `test` recipe runs the solution with sample data; it does
not assert expected answers.
