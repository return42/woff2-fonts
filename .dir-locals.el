;;; .dir-locals.el
((nil
  . ((indent-tabs-mode . t)
     (fill-column . 80)
     ))
 (python-mode
  . ((indent-tabs-mode . nil)
     (flycheck-pylintrc . ".pylintrc")
     (flycheck-python-pylint-executable . "python3")
    ))
)
