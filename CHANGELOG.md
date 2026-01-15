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

### ⚡ New Feature: Command Bundling
- **Streamlined Flags:** Support for grouped operations (e.g., `-si`, `-syu`).
- **Smart Logic:** The engine now parses multiple flags simultaneously to execute sequential tasks (Sync + Update + Install) in a single execution line.
