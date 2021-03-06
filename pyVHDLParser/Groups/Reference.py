# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python functions:   A streaming VHDL parser
#
# Description:
# ------------------------------------
#		TODO:
#
# License:
# ==============================================================================
# Copyright 2007-2017 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
# load dependencies
from pyVHDLParser.Blocks.Reference          import Library, Use
from pyVHDLParser.Groups                    import ParserState, BlockParserException, Group

class LibraryGroup(Group):
	@classmethod
	def stateParse(cls, parserState: ParserState):
		for block in parserState.GetBlockIterator:
			if isinstance(block, Library.EndBlock):
				parserState.NextGroup = cls(parserState.LastGroup, parserState.BlockMarker, block)
				parserState.Pop()
				return

		raise BlockParserException("End of library clause not found.", block)


class UseGroup(Group):
	@classmethod
	def stateParse(cls, parserState: ParserState):
		for block in parserState.GetBlockIterator:
			if isinstance(block, Use.EndBlock):
				parserState.NextGroup = cls(parserState.LastGroup, parserState.BlockMarker, block)
				parserState.Pop()
				return

		raise BlockParserException("End of library clause not found.", block)
