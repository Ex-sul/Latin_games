from kivy.config import ConfigParser


class FixedConfig(ConfigParser):
    def read(self, filename):
        '''Read only one filename. In contrast to the original ConfigParser of
                Python, this one is able to read only one file at a time. The last
                read file will be used for the :meth:`write` method.
                .. versionchanged:: 1.9.0
                    :meth:`read` now calls the callbacks if read changed any values.
                '''
        if not isinstance(filename, string_types):
            raise Exception('Only one filename is accepted ({})'.format(
                string_types.__name__))
        self.filename = filename
        # If we try to open directly the configuration file in utf-8,
        # we correctly get the unicode value by default.
        # But, when we try to save it again, all the values we didn't changed
        # are still unicode, and then the PythonConfigParser internal do
        # a str() conversion -> fail.
        # Instead we currently to the conversion to utf-8 when value are
        # "get()", but we internally store them in ascii.
        # with codecs.open(filename, 'r', encoding='utf-8') as f:
        #         #    self.readfp(f)
        old_vals = {sect: {k: v for k, v in self.items(sect)} for sect in
                    self.sections()}
        PythonConfigParser.read(self, filename, encoding='utf8')

        # when reading new file, sections/keys are only increased, not removed
        f = self._do_callbacks
        for section in self.sections():
            if section not in old_vals:  # new section
                for k, v in self.items(section):
                    f(section, k, v)
                continue

            old_keys = old_vals[section]
            for k, v in self.items(section):  # just update new/changed keys
                if k not in old_keys or v != old_keys[k]:
                    f(section, k, v)

