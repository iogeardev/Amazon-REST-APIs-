let
    // Removes repeated header rows in combined CSVs (common for exported reports)
    Source = #"Previous Step",
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Cleaned = Table.SelectRows(Promoted, each [SKU] <> "SKU" and [SKU] <> null)
in
    Cleaned
