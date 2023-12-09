(define (if-program condition if-true if-false)
  (if (eval condition)
      if-true
      if-false
  )
)



(define (pow-expr n p)
  (if (= p 0)
      1
      `(* ,(pow-expr n (- p 1)) ,n)))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr)
  (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
    (cond ((< (eval first) (eval second)) (cons op (cons second (cons first rest))))
          (else (cons op (cons first (cons second rest)))))))
