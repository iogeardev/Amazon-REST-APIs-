let
    // SharePoint Folder loader (Modeled/latest)
    // Replace with your SharePoint site URL and folder path filter.
    Source = SharePoint.Files("https://YOURTENANT.sharepoint.com/sites/YOURSITE", [ApiVersion = 15]),
    Filtered = Table.SelectRows(Source, each Text.Contains([Folder Path], "/Amazon/SPAPI/exports/modeled/") and Text.Contains([Folder Path], "/latest/")),
    Visible = Table.SelectRows(Filtered, each [Attributes]?[Hidden]? <> true),
    // Choose one dataset folder at a time by adding an additional filter on [Folder Path]
    // Example: and Text.Contains([Folder Path], "/seller/orders/")
    ContentOnly = Table.SelectColumns(Visible, {"Name","Folder Path","Content"}),
    AddedTables = Table.AddColumn(ContentOnly, "Data", each Csv.Document([Content],[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv])),
    Expanded = Table.ExpandTableColumn(AddedTables, "Data", {"Column1"}, {"Column1"})
in
    Expanded
