let
    // SharePoint Folder loader (Raw)
    Source = SharePoint.Files("https://YOURTENANT.sharepoint.com/sites/YOURSITE", [ApiVersion = 15]),
    Filtered = Table.SelectRows(Source, each Text.Contains([Folder Path], "/Amazon/SPAPI/exports/raw/")),
    Visible = Table.SelectRows(Filtered, each [Attributes]?[Hidden]? <> true)
in
    Visible
