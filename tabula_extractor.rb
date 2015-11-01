load 'constants'

file_names.each do |file_name|
    output_file_name = file_name.gsub('.pdf', '.csv')
    output_file = open("csv_files/#{output_file_name}", 'w')
    extractor = Tabula::Extraction::ObjectExtractor.new("pdf_files/#{file_name}")
    extractor.extract.each_with_index do |pdf_page, page_index|
      # we should play with these settings to see if it gets us better results
      page_areas = [[250, 0, 325, 1700]]
      scale_factor = pdf_page.width / 1700
      vertical_ruling_locations = [0, 360, 506, 617, 906, 1034, 1160, 1290, 1418, 1548] #column locations
      vertical_rulings = vertical_ruling_locations.map{|n| Tabula::Ruling.new(0, n * scale_factor, 0, 1000)}
      page_areas.each do |page_area|
        output_file << pdf_page.get_area(page_area).get_table(:vertical_rulings => vertical_rulings).to_csv
        output_file << "\n\n"
      end
    end
    extractor.close!
    output_file.close
end
