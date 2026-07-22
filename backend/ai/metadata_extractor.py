import re


class MetadataExtractor:

    def extract(
        self,
        text,
        pages
    ):

        return {

            "pages": pages,

            "characters": len(text),

            "words": len(text.split()),

            "estimated_read_time":
                round(len(text.split()) / 200, 1)
        }


metadata_extractor = MetadataExtractor()