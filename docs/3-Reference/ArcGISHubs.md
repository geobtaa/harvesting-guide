# ArcGIS Hubs

ArcGIS Hub is an architecture consisting of ArcGIS Enterprise at the global level, which provides the foundation for hosting services on ArcGIS Server via REST API, portals, and data stores. It is a platform designed for creating and sharing geospatial data with the public, and can be used by organizations, communities, and government agencies. The architecture of ArcGIS Hub allows for centralized management and control of data, making it easy to manage and share data across multiple portals.


* ArcGIS Hub architecture (consisting of ArcGIS Enterprise at the global level, and then hosting these services on ArcGIS Server via REST API, Portals, and Data Stores (also ArcGIS Server)
* Vs ArcGIS Online (cloud-based and usable in fieldwork) BUT incomparable as Open services URLs are more stable in portals than from IDs, because of REST API web points.
* IDs are not persistent and metadata from ArcGIS Open Portals (via different agencies) varies, when these change, links break
* Original referenced portals that are updated or re-published retain the same ID, but not if deleted (if content is re-uploaded with a new ID administered).
* ArcGIS Online and ArcGIS Hubs if using ArcGIS Contents pane retain metadata for upload.
* Organizations should adhere to one metadata standard (ISO, ArcGIS, etc) so it would be efficient in upgrading or transitioning from an ArcGIS Server to another app based portal.
