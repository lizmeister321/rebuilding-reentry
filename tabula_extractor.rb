require 'tabula'

file_names = []
IO.readlines('file_names').each do |line|
  file_names << line.chomp
end

file_names.each do |file_name|
    output_file_name = file_name.gsub('.pdf', '.csv')
    output_file = open("csv_files/#{output_file_name}", 'w')
    puts "Extracting #{file_name} to #{output_file_name}"
    extractor = Tabula::Extraction::ObjectExtractor.new("pdf_files/#{file_name}", :all)
    extractor.extract.each do |pdf_page|
      # we should play with these settings to see if it gets us better results
      pdf_page.spreadsheets.each do |spreadsheet|
        output_file << spreadsheet.to_csv
        output_file << "\n\n"
      end
    end
    extractor.close!
    output_file.close
end
