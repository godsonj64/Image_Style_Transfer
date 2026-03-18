from enum import Enum


class PolicyDecision(str, Enum):
    allow = "allow"
    deny = "deny"
    approval_required = "approval_required"
    dry_run_only = "dry_run_only"


class PolicyEngine:
    HIGH_RISK_TOOLS = {
        "send_email",
        "external_upload",
        "run_shell_guarded",
        "delete_file_safe",
    }

    def decide(self, tool_name: str, workspace_scoped: bool = True) -> PolicyDecision:
        if tool_name in self.HIGH_RISK_TOOLS:
            return PolicyDecision.approval_required
        if not workspace_scoped:
            return PolicyDecision.deny
        return PolicyDecision.allow
