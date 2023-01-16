BIA Zarr annotation
===================

Code for annotating BIA images based on Zarr metadata.

Install
-------

Install dependencies with:

    pip install -r requirements

Use
---

Create annotations for a study with:

    python scripts/annotate_study_from_zarr S-BIAD144

Set rendering information from a the OME-Zarr file for an image with:

    python scripts/set_rendering_info_from_ome_ngff.py S-BSST522 IM1

Then generate a thumbnail/preview with:

    python scripts/generate_thumbnail.py S-BSST522 IM1