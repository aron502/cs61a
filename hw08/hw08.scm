(define (ascending? s)
    (define (helper prev s)
        (if (null? s)
            #t
            (let ((cur (car s)))
                (if (> prev cur)
                    #f
                    (helper cur (cdr s))))))
    (if (null? s)
        #t
        (helper (car s) s))
)

(define (my-filter pred s)
    (if (null? s) nil
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
    (define (helper lst1 lst2 flag)
        (cond ((null? lst1) lst2)
              ((null? lst2) lst1)
              ((= flag 1) (cons (car lst1) (helper (cdr lst1) lst2 (- 1 flag))))
              (else (cons (car lst2) (helper lst1 (cdr lst2) (- 1 flag))))))
    (helper lst1 lst2 1))

(define (no-repeats s)
    (define (mem? val s)
        (if (null? s)
            #f
            (if (= (car s) val)
                #t
                (mem? val (cdr s)))))

    (define lst nil)
    (filter (lambda (x)
        (cond ((mem? x lst) #f)
              (else (set! lst (cons x lst)) #t))) s))
