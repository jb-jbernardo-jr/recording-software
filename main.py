import pytz

def record(DEFAULT_CAMERA=0, FORMAT = '%Y%m%d%H%M%S', TIMEZONE = pytz.timezone('America/Manaus'), EXTENSION='.avi', VIDEOSIZE=900):
    import os, cv2, datetime, time

    OUTPUT_FOLDER = os.path.join( os.getcwd(), 'Records' )
    if( not os.path.exists(OUTPUT_FOLDER) ):
        os.makedirs( OUTPUT_FOLDER )

    cap = cv2.VideoCapture(DEFAULT_CAMERA)
    cv2.namedWindow('Recording Software')

    while( cv2.getWindowProperty('Recording Software', cv2.WND_PROP_VISIBLE) <= 1 ):

        START = time.time()
        END = 0

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        FILENAME = TIMEZONE.localize( datetime.datetime.now() ).strftime(FORMAT) + EXTENSION
        OUTPUT_FILE = f'{OUTPUT_FOLDER}/{FILENAME}'
        out = cv2.VideoWriter(OUTPUT_FILE, fourcc, 20.0, (int( cap.get(3) ), int( cap.get(4) )) )

        while( ( END - START ) <= VIDEOSIZE ):

            ret, frame = cap.read()

            if(ret): 

                # cv2.imshow('Recording Software', frame)
                
                out.write(frame)

            else:

                break

            END = time.time()

        print(f'Vídeo {FILENAME} salvo com sucesso!')

    cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':

    record()
