
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; MODULE      : init-sympy.scm
;; DESCRIPTION : Initialize the SymPy plugin
;; COPYRIGHT   : (C) 2019-2022  Darcy Shen
;;
;; This software falls under the GNU general public license version 3 or later.
;; It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
;; in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (sympy-serialize lan t)
    (with u (pre-serialize lan t)
      (with s (texmacs->code (stree->tree u) "SourceCode")
        (string-append s "\n<EOF>\n"))))

(define (sympy-launcher)
  (if (url-exists? "$TEXMACS_HOME_PATH/plugins/sympy")
      (string-append "python3 "
                     (getenv "TEXMACS_HOME_PATH")
                     "/plugins/sympy/bin/sympy.pex")
      (string-append "python3 "
                     (getenv "TEXMACS_PATH")
                     "/plugins/sympy/bin/sympy.pex")))

(plugin-configure sympy
  (:require (python-command))
  (:launch ,(sympy-launcher))
  (:serializer ,sympy-serialize)
  (:tab-completion #t)
  (:session "SymPy"))
