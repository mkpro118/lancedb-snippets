import dataclasses
import pathlib

from typing import Optional

from snippets.languages import Language


@dataclasses.dataclass
class Snippet:
    text: str
    language: Language
    filename: Optional[pathlib.Path] = None

    def __post_init__(self):
        if self.filename is None:
            return

        filename = pathlib.Path(self.filename)

        self.filename = filename

    @classmethod
    def from_file(cls, filepath: str | pathlib.Path) -> "Snippet":
        if not isinstance(filepath, pathlib.Path):
            filepath = pathlib.Path(filepath).resolve()
        filepath.resolve()

        if not filepath.is_file():
            raise ValueError(
                f"{filepath} does not exist or is not a regular file"
            )

        try:
            language = Language.from_file_extension(filepath)
        except ValueError:
            raise ValueError(
                "Your file seems to be a language that is not yet supported"
            )

        with open(str(filepath)) as f:
            text = f.read()

        return cls(text=text, language=language, filename=filepath)

    def to_dict(self) -> dict[str, str]:
        return {
            "text": self.text,
            "language": self.language.value,
            "filename": str(self.filename),
        }
