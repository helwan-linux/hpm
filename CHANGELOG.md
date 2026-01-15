# Changelog - hpm v1.1

## [1.1.0] - 2026-01-15
### 🚀 Core Enhancements
- **Optimized Dependency Resolution:** Refactored the internal engine to handle complex package trees with higher efficiency.
- **Improved AUR Integration:** Enhanced the interaction layer with Arch User Repository for more stable builds.

### 🛠 Fixes & Stability
- **Connection Persistence:** Mitigated the "Connection reset" issues by implementing a more robust retry mechanism.
- **Path Sanitization:** Resolved critical bugs related to absolute/relative path handling during installation.

### 📝 Documentation & UX
- **Verbose Output:** Added detailed logging for troubleshooting failed builds.
- **User Guide:** Completed the first comprehensive manual for end-users.

### ⚡ New Feature: Command Chaining (then)
- **Sequential Execution:** Added full support for linking multiple commands using the "then" keyword (e.g., `hpm sync then update`).
- **Smart Logic:** The engine now ensures that chained commands are executed in the correct logical order to prevent build errors.
