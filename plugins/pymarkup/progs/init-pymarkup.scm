
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; MODULE      : init-markup.scm
;; DESCRIPTION : Initialize the 'markup' plugin
;; COPYRIGHT   : (C) 1999  Joris van der Hoeven
;;
;; This software falls under the GNU general public license version 3 or later.
;; It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
;; in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (python-launcher)
  (if (url-exists? "$TEXMACS_HOME_PATH/plugins/pymarkup")
      (string-append "python3 " (getenv "TEXMACS_HOME_PATH")
                     "/plugins/pymarkup/bin/pymarkup.pex")
      (string-append "python3 " (getenv "TEXMACS_PATH")
                     "/plugins/pymarkup/bin/pymarkup.pex")))

(plugin-configure pymarkup
  (:require (url-exists-in-path? "python"))
  (:launch ,(python-launcher))
  (:session "PyMarkup"))
