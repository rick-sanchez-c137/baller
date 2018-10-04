from openalpr import Alpr
from argparse import ArgumentParser
import os, fnmatch

def plater(image_paths) -> bool:
    alpr = None
    found_count = 0     
    image_dir = "./images/"
    try:
        alpr = Alpr("us", "./baller.alpr.config", "/usr/share/openalpr/runtime_data")

        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
            print("Using OpenALPR " + alpr.get_version())

            alpr.set_top_n(5)
            alpr.set_default_region("tx")
            alpr.set_detect_region(True)


            for entry in image_paths:  
                jpeg_bytes = open(os.path.join(image_dir, entry), "rb").read()
                results = alpr.recognize_array(jpeg_bytes)

                # print ("kakakak \n\n\n")
                # print (results['results'])
                # for plate in results['results']:
                #     i += 1
                #     print("Plate #%d" % i)
                #     print("   %12s %12s" % ("Plate", "Confidence"))
                #     for candidate in plate['candidates']:
                #         prefix = "-"
                #         if candidate['matches_template']:
                #             prefix = "*"

                #         print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
                
                if len(results['results']) > 0:
                    found_count += 1

        return found_count > 0

    finally:
        if alpr:
            alpr.unload()
