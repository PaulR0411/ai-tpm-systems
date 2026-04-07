import json
from pathlib import Path

def main():
    data = json.loads(Path("examples/sample_updates.json").read_text())
    updates = data["updates"]

    print("AI TPM Systems Demo\n")
    print("Input updates:")
    for u in updates:
        print(f"- {u}")

    print("\nStructured output:")
    print("Progress:")
    print("- integration work ongoing but delayed")

    print("\nBlockers:")
    print("- API dependency delay")
    print("- design blocked on requirements")

    print("\nRisks:")
    print("- dependency risk: API delay impacting timeline")
    print("- ownership risk: unclear infra ownership")

    print("\nActions:")
    print("- assign infra owner within 48 hours")
    print("- escalate API dependency")
    print("- finalize requirements")

if __name__ == "__main__":
    main()
