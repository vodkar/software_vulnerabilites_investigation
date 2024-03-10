import polars as pl


def enrich_commits_data(commits):
    commits = commits.with_columns(pl.col("cve_id").str.split(by="-").list.get(0).str.to_integer().alias("year"))
    # extract file extension
    commits = commits.with_columns(pl.col("file").str.extract(r".*\.(.*)", group_index=1).alias("file_extension"))
    commits = commits.with_columns(
        pl.col("file_extension")
        .replace(
            {
                "c": "C",
                "h": "C",
                "cpp": "C++",
                "hpp": "C++",
                "cc": "C++",
                "hh": "C++",
                "java": "Java",
                "py": "Python",
                "js": "JavaScript",
                "ts": "TypeScript",
                "tsx": "TypeScript",
                "go": "Go",
                "rb": "Ruby",
                "php": "PHP",
                "phtml": "PHP",
                "cs": "C#",
                "swift": "Swift",
                "scala": "Scala",
                "rs": "Rust",
                "kt": "Kotlin",
                "clj": "Clojure",
                "cljc": "Clojure",
                "cljs": "Clojure",
                "groovy": "Groovy",
                "scala": "Scala",
                "dart": "Dart",
                "lua": "Lua",
                "r": "R",
                "sh": "Shell",
                "bash": "Shell",
                "zsh": "Shell",
                "ps1": "PowerShell",
                "psm1": "PowerShell",
                "bat": "Batchfile",
                "cmd": "Batchfile",
                "awk": "Awk",
                "yml": "YAML",
                "yaml": "YAML",
                "json": "JSON",
                "xml": "XML",
                "html": "HTML",
                "css": "CSS",
                "scss": "SCSS",
                "less": "Less",
                "styl": "Stylus",
                "sql": "SQL",
                "pl": "Perl",
                "jl": "Julia",
                "hcl": "HCL",
                "tf": "terraform",
            }
        )
        .alias("language")
    ).filter(pl.Expr.not_(pl.col("language").is_in(["txt", "md", "JSON", "YAML"])))
    return commits
