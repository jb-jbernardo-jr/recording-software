def record(DEFAULT_CAMERA=0):
    import os, cv2

    OUTPUT_FOLDER = os.path.join( os.getcwd(), 'Records' )
    if( not os.path.exists(OUTPUT_FOLDER) ):
        os.makedirs( OUTPUT_FOLDER )

    cap = cv2.VideoCapture(DEFAULT_CAMERA)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    FILENAME = 'output.avi'
    OUTPUT_FILE = f'{OUTPUT_FOLDER}/{FILENAME}'
    out = cv2.VideoWriter(OUTPUT_FILE, fourcc, 20.0, (int( cap.get(3) ), int( cap.get(4) )) )

    while(True):

        ret, frame = cap.read()

        if(ret): 

            cv2.imshow('Recording Software', frame)
            
            out.write(frame)

            if( cv2.waitKey(1) & 0xFF == ord('q') ):
                break

        else:

            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':

    record()
